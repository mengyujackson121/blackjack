from typing import List
import random
import card
import json
from pprint import pprint
from player import Player

Hand = List[card.Card]


def main():
    with open('conf.json') as data_file:
        data = json.load(data_file)
        len(data["players"])

    size = len(data["players"])
    list_player = []
    s17 = dealer_type(data["dealer"]["strategy"])

    for i in range(size):
        p_data = data["players"][i]
        new_player = Player(name=p_data["name"], money=int(p_data["starting_money"]), rank_only=p_data["rank_only"], strategy=p_data["strategy"])
        list_player.append(new_player)

    while input("Wanna Start a New Game? (q for quit, any key contiune...)") != 'q':
        card_deck = start_game()
        for p in list_player:
            down(p)
        for p in list_player:
            p.hand = []
            get_start_hands(card_deck, p.hand)
        dealer_hand = []
        get_start_hands(card_deck, dealer_hand)
        for p in list_player:
            player_turn(card_deck, p)
        dealer_turn(dealer_hand, card_deck, s17)
        for p in list_player:
            win = check_winner(p, dealer_hand)
            give_money(win, p)
        next_list = []
        for p in list_player:
            if is_enough_money(p):
                next_list.append(p)
        list_player = next_list
        if len(list_player) == 0:
            quit()


def dealer_type(strategy):
    if strategy == "S17":
        return True
    else:
        return False


def display_list(hand, rank_only):
    if rank_only:
        return [card.rank for card in hand]
    else:
        return [str(card) for card in hand]


def winner(play, deal):
    if cal_value(play) > cal_value(deal):
        print("Player Win!")
        return True

    elif cal_value(play) == cal_value(deal):
        print("Tie Dealer Win!")
        return False

    else:
        print("Dealer Win!")
        return False


def is_soft(hand):
    if len(cal_all_value(hand)) == 1:
        return False
    else:
        return True


def cal_value(hand: Hand):
    return cal_all_value(hand)[-1]


def cal_all_value(hand: Hand):
    num_aces = 0
    value = 0
    value_list = []
    for card_v in hand:

        rank = card_v.rank

        if rank == "10" or rank == "J" or rank == "Q" or rank == "K":
            value = value + 10
        elif rank == "A":
            value = value + 1
            num_aces = num_aces + 1
        else:
            value = value + int(rank)
    value_list.append(value)
    count = 0
    while count < num_aces:
        value = value + 10
        if value <= 21:
            value_list.append(value)
            count = count + 1
        else:
            break
    return value_list


def get_card(role, card_deck):
    role.append(card_deck.pop(random.randrange(len(card_deck))))


def result(player: Player, dealer_hand,):
    print("Player: ", display_list(player.hand, player.rank_only), cal_value(player.hand),
          'Value: ', cal_value(player.hand))
    print("Dealer: ", display_list(dealer_hand, player.rank_only), cal_value(dealer_hand),
          'Value: ', cal_value(dealer_hand))


def down(player: Player):
    while True:
        try:
            val = int(input(player.name + ": How much down? (1 - " + str(player.money) + "): "))
            if val in range(1, player.money + 1):
                player.bet_amount = val
                return
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")


def start_game():
    card_deck = card.standard_deck()
    return card_deck


# def choice_rank(player: Player):
#     if input(player.name + ': Rank or Not? (r to Rank only: )') == 'r':
#         player.rank_only = True
#     else:
#         player.rank_only = False


def get_player_size(size):
    while 1 > size or 5 < size:
        try:
            size = int(input("Please enter your players (1 - 5) : "))
            print("Number of The Player: " + str(size))
            return size
        except ValueError:
            return get_player_size(size)


def get_start_hands(card_deck, hand):
    while len(hand) < 2:
        get_card(hand, card_deck)


def player_turn(card_deck, player: Player):
    print(display_list(player.hand, player.rank_only), 'Value: ', cal_value(player.hand))
    while input(player.name + ': Hit or Stay? (h to hit, any else for stay: )') == 'h':
        get_card(player.hand, card_deck)
        print(display_list(player.hand, player.rank_only), 'Value: ', cal_value(player.hand))
        if cal_value(player.hand) >= 21:
            return


def dealer_turn(dealer, card_deck, s17):
    if s17 is True:
        while cal_value(dealer) < 17:
            get_card(dealer, card_deck)

    else:
        if cal_value(dealer) <= 16:
            get_card(dealer, card_deck)
            dealer_turn(dealer, card_deck, s17)
        elif cal_value(dealer) == 17 and is_soft(dealer) is True:
            get_card(dealer, card_deck)
            dealer_turn(dealer, card_deck, s17)
        else:
            return


def check_winner(player: Player, dealer):
    if cal_value(player.hand) <= 21 and cal_value(dealer) <= 21:
        result(player, dealer)
        return winner(player.hand, dealer)

    elif cal_value(player.hand) > 21:
        result(player, dealer)
        print("Player Lose! Over 21!")
        return False

    else:
        result(player, dealer)
        print("Dealer Lose! Over 21!")
        return True


def give_money(win, player: Player):
    if win is True and len(player.hand) == 2:
        player.money = player.money + player.bet_amount * 2
    elif win is True:
        player.money = player.money + player.bet_amount
    else:
        player.money = player.money - player.bet_amount
    print("total :", player.money)


def is_enough_money(player: Player):
    if player.money <= 0:
        print(player.name + " Don't have money!")
        return False
    else:
        return True


if __name__ == '__main__':
    main()
