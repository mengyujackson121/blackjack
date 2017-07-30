from typing import List
import random
import card
Hand = List[card.Card]

rank_only = False
stop_game = False
money = 100


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


def get_card(role, card):
    role.append(card.pop(random.randrange(len(card))))

def result(player_, dealer_):
    print("Player: ", player, cal_value(player), 'Value: ', cal_value(player_))
    print("Dealer: ", dealer, cal_value(dealer), 'Value: ', cal_value(dealer_))


def down(money_):
    val = int(input("How much down? (1 - " + str(money_) + "): "))
    if 0 >= val or val > money_:
        print("Error: You don't have that much Money!")
        return down(money_)
    return val


while input("Wanna Start a New Game? (q for quit, any key contiune...)") != 'q':
    put_down = down(money)
    print(put_down)
    win = False
    bj = False
    card_deck = card.standard_deck()
    if input('Rank or Not? (r to Rank only: )') == 'r':
        rank_only = True

    else:
        rank_only = False

    player = []
    dealer = []

    while len(dealer) < 2:
        get_card(player, card_deck)
        get_card(dealer, card_deck)

    if len(dealer) == 2 and len(player) == 2:
        print("Player: ", player, 'Value: ', cal_value(player))
        dealer_hand_show = [dealer[0]]
        print("Dealer: ", dealer_hand_show, 'Value: ', cal_value(dealer_hand_show))
        if cal_value(dealer) == 21:
            print("Dealer Win!")
            result(player, dealer)
        elif cal_value(player) == 21 and cal_value(dealer) != 21:
            print("BlackJack!")
            bj = True
            win = True
            result(player, dealer)

    while input('Hit or Stay? (h to hit, any else for stay: )') == 'h':
        get_card(player, card_deck)
        print(player, 'Value: ', cal_value(player))
        if cal_value(player) == 21:
            print("Player Win! 21 point!")
            win = True
            result(player, dealer)
            break
        elif cal_value(player) > 21:
            result(player, dealer)
            break

    while cal_value(dealer) < 17:
        get_card(dealer, card_deck)
        if cal_value(dealer) > 21:
            win = True
            break

    if cal_value(player) <= 21 and cal_value(dealer) <= 21:
        result(player, dealer)
        win = winner(player, dealer)

    elif cal_value(player) > 21:
        result(player, dealer)
        print("Player Lose! Over 21!")

    else:
        result(player, dealer)
        print("Dealer Lose! Over 21!")

    if win is True and bj is True:
        money = money + put_down * 2
    elif win is True:
        money = money + put_down
    else:
        money = money - put_down
    print("total :", money)
    if money <= 0:
        quit()
