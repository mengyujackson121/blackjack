from typing import List
import random
import card
import json
from player import Player
import argparse
Hand = List[card.Card]


def main(data):
    size = len(data["players"])
    list_player = []
    total_round = data["max_rounds"]
    tie_behavior = data["tie_behavior"]
    blackjack_multiplier = data["blackjack_multiplier"]

    for i in range(size):
        p_data = data["players"][i]
        new_player = Player(name=p_data.get("name", 'DP'),
                            money=p_data.get("starting_money", 100),
                            rank_only=p_data.get("rank_only", True),
                            strategy=p_data.get("strategy", 'H17'),
                            betting_strategy=p_data.get("betting_strategy", 'ask'))
        list_player.append(new_player)

    while input("Wanna Start a New Game? (q for quit, any key contiune...)") != 'q':
        start = 0
        for p in list_player:
            p.bet_amount = 0
        while start < total_round:
            start = start + 1
            for p in list_player:
                if p.betting_strategy == 'ask':
                    down(p)
                elif p.betting_strategy == 'minimum':
                    val = data['minimum_bet']
                    if val in range(1, int(p.money) + 1):
                        p.bet_amount = val
                    else:
                        p.bet_amount = p.money
                else:
                    val = data['maximum_bet']
                    if val in range(1, int(p.money) + 1):
                        p.bet_amount = val
                    else:
                        p.bet_amount = int(p.money)
            print("GAME: ", start)
            card_deck = start_game()
            for p in list_player:
                get_start_hands(card_deck, p.hand)
            dealer_hand = []
            get_start_hands(card_deck, dealer_hand)
            for p in list_player:
                if p.strategy == 'player':
                    player_turn(card_deck, p)
                else:
                    dealer_turn(p.hand, card_deck, p.strategy)

            dealer_turn(dealer_hand, card_deck, data['dealer']['strategy'])
            for p in list_player:
                result = check_winner(p, dealer_hand, tie_behavior)
                give_money(result, p, blackjack_multiplier)
            next_list = []
            for p in list_player:
                if is_enough_money(p):
                    next_list.append(p)
            list_player = next_list
            if len(list_player) == 0:
                quit()
            for p in list_player:
                if check_winner(p, dealer_hand, tie_behavior) == "player_win":
                    print(">>>", p.name, "WIN!  Total money: ", p.money)
                elif check_winner(p, dealer_hand, tie_behavior) == "dealer_win":
                    print(">>>", p.name, "LOSE!  Total money: ", p.money)
                else:
                    print(">>>NO WINNER! Tie Game....", p.name, p.money)


def display_list(hand, rank_only):
    if rank_only:
        return [c.rank for c in hand]
    else:
        return [str(c) for c in hand]


def winner(play, deal, tie_behavior):
    if cal_value(play) > cal_value(deal):
        return "player_win"
    elif cal_value(play) == cal_value(deal):
        return tie_behavior
    else:
        return "dealer_win"


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
    print(player.name, display_list(player.hand, player.rank_only),
          "Value: ", cal_value(player.hand),
          "Bet Amount: ", player.bet_amount,
          "Total Money: ", player.money)
    print("Dealer", display_list(dealer_hand, player.rank_only),
          'Value: ', cal_value(dealer_hand))


def down(player: Player):
    while True:
        try:
            val = int(input(player.name + ": How much down for next Game? (1 - " + str(player.money) + "): "))
            if val in range(1, int(player.money) + 1):
                player.bet_amount = val
                return
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")


def start_game():
    card_deck = card.standard_deck()
    return card_deck


def get_start_hands(card_deck, hand):
    while len(hand) < 2:
        get_card(hand, card_deck)


def player_turn(card_deck, player: Player):
    print(player.name, ' ', display_list(player.hand, player.rank_only), 'Value: ', cal_value(player.hand))
    while input(player.name + ': Hit or Stay? (h to hit, any else for stay: )') == 'h':
        get_card(player.hand, card_deck)
        print(display_list(player.hand, player.rank_only), 'Value: ', cal_value(player.hand))
        if cal_value(player.hand) >= 21:
            return


def dealer_turn(dealer, card_deck, strategy):
    if strategy == 'S17':
        while cal_value(dealer) < 17:
            get_card(dealer, card_deck)

    else:
        if cal_value(dealer) <= 16:
            get_card(dealer, card_deck)
            dealer_turn(dealer, card_deck, strategy)
        elif cal_value(dealer) == 17 and is_soft(dealer) is True:
            get_card(dealer, card_deck)
            dealer_turn(dealer, card_deck, strategy)
        else:
            return


def check_winner(player: Player, dealer, tie_behavior):
    if cal_value(player.hand) <= 21 and cal_value(dealer) <= 21:
        result(player, dealer)
        return winner(player.hand, dealer, tie_behavior)

    elif cal_value(player.hand) > 21:
        result(player, dealer)
        return "dealer_win"

    else:
        result(player, dealer)
        return "player_win"


def give_money(result, player: Player, blackjack_multiplier):
    if result == "player_win" and len(player.hand) == 2 and cal_value(player.hand) == 21:
        player.money = int(player.money + player.bet_amount * blackjack_multiplier)
    elif result == "player_win":
        player.money = player.money + player.bet_amount
    elif result == "dealer_win":
        player.money = player.money - player.bet_amount
    else:
        player.money = player.money


def is_enough_money(player: Player):
    if player.money <= 0:
        print(player.name + " Don't have money!")
        return False
    else:
        return True


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="read from this file")
    args = parser.parse_args()
    if args.config:
        with open(args.config) as data_file:
            __data = json.load(data_file)
    else:
        print("No config file!")
        quit()
    main(__data)
