from typing import List
import random
import card
Hand = List[card.Card]


def main():
    rank_only = False
    money = 100
    shift = 0

    card_deck, put_down = start_game(money)
    rank_only = choice_rank()
    # shift = get_player_size(shift)
    player, dealer = get_start_hands(card_deck)
    player_turn(player, dealer, card_deck, rank_only)
    dealer_turn(dealer, card_deck)
    win = check_winner(player, dealer, rank_only)
    money = give_money(win, money, put_down, player)
    is_enough_money(money)


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


def cal_value(hand: Hand):
    num_aces = 0
    value = 0

    for card_v in hand:
        rank = card_v.rank

        if rank == "10" or rank == "J" or rank == "Q" or rank == "K":
            value = value + 10
        elif rank == "A":
            num_aces += 1
            value = value + 1
        else:
            value = value + int(rank)

    for i in range(num_aces):
        if value <= 11:
            value += 10

    return value


def get_card(role, card_deck):
    role.append(card_deck.pop(random.randrange(len(card_deck))))


def result(player_, dealer_, rank_only):
    print("Player: ", display_list(player_, rank_only), cal_value(player_), 'Value: ', cal_value(player_))
    print("Dealer: ", display_list(dealer_, rank_only), cal_value(dealer_), 'Value: ', cal_value(dealer_))


def down(money_):
    val = int(input("How much down? (1 - " + str(money_) + "): "))
    if 0 >= val or val > money_:
        print("Error: You don't have that much Money!")
        return down(money_)
    return val


def start_game(money):
    while input("Wanna Start a New Game? (q for quit, any key contiune...)") != 'q':
        put_down = down(money)
        print(put_down)
        card_deck = card.standard_deck()
        return card_deck, put_down


def choice_rank():
    if input('Rank or Not? (r to Rank only: )') == 'r':
        rank_only = True
    else:
        rank_only = False
    return rank_only


def get_player_size(shift):
    while 1 > shift or 5 < shift:
        try:
            shift = int(input("Please enter your players (1 - 5) : "))
            return shift
        except ValueError:
            get_player_size(shift)


def get_start_hands(card_deck):
    dealer = []
    player = []
    while len(dealer) < 2:
        get_card(player, card_deck)
        get_card(dealer, card_deck)
    return player, dealer


def player_turn(player, dealer, card_deck, rank_only):
    while input('Hit or Stay? (h to hit, any else for stay: )') == 'h':
        get_card(player, card_deck)
        print(display_list(player, rank_only), 'Value: ', cal_value(player))
        if cal_value(player) == 21:
            print("Player Win! 21 point!")
            result(player, dealer, rank_only)
            return

        elif cal_value(player) > 21:
            result(player, dealer, rank_only)
            return


def dealer_turn(dealer, card_deck):
    while cal_value(dealer) < 17:
        get_card(dealer, card_deck)
        if cal_value(dealer) > 21:
            return


def check_winner(player, dealer, rank_only):
    if cal_value(player) <= 21 and cal_value(dealer) <= 21:
        result(player, dealer, rank_only)
        return winner(player, dealer)

    elif cal_value(player) > 21:
        result(player, dealer, rank_only)
        print("Player Lose! Over 21!")
        return False

    else:
        result(player, dealer, rank_only)
        print("Dealer Lose! Over 21!")
        return True


def give_money(win, money, put_down, player):
    if win is True and len(player) == 2:
        money = money + put_down * 2
    elif win is True:
        money = money + put_down
    else:
        money = money - put_down
    print("total :", money)
    return money


def is_enough_money(money):
    if money <= 0:
        quit()


if __name__ == '__main__':
    main()
