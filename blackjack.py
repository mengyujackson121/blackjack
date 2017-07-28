# one deck, new deck each new game
import random


rank_only = False
stop_game = False

def cal_value(hand):
    num_aces = 0
    value = 0
    for card_v in hand:
        if rank_only is True:
            rank = card_v
            if rank == "10" or rank == "J" or rank == "Q" or rank == "K":
                value = value + 10
            elif rank == "A":
                num_aces += 1
                value = value + 1
            else:
                value = value + int(rank)
        else:
            rank = card_v[:-1]
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


def get_card(role,card):
    role.append(card.pop(random.randrange(len(card))))

def result(player, dealer):
    print("Player: ", player, cal_value(player), 'Value: ', cal_value(player))
    print("Dealer: ", dealer, cal_value(dealer), 'Value: ', cal_value(dealer))

while input("Wanna Start a New Game? (q for quit, any key contiune...)") != 'q':
    game_over = False

    if input('Rank or Not? (r to Rank only: )') == 'r':
        card_deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]*4
        rank_only = True

    else:
        card_deck = [rank + suit
                     for rank in ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
                     for suit in ("C", "D", "H", "S")]
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

        if cal_value(player) == 21 and cal_value(dealer) != 21:
            print("3) Twenty-One!")
            result(player, dealer)
            game_over = True

        elif cal_value(dealer) == 21:
            print("2) Twenty-One!::Dealer Win!")
            result(player, dealer)
            game_over = True

    while input('Hit or Stay? (h to hit, any else for stay: )') == 'h':
            get_card(player, card_deck)
            print(player, 'Value: ', cal_value(player))
            if cal_value(player) > 21:
                game_over = True
                break

    while cal_value(dealer) < 17:
            get_card(dealer, card_deck)
            if cal_value(dealer) > 21:
                game_over = True
                break

    if cal_value(player) == cal_value(dealer):
        print("4) Tie! Dealer Win!")
        result(player, dealer)
        game_over = True

    else:
        if game_over is False and cal_value(player) > cal_value(dealer) and cal_value(player) <= 21:
            print("7) WIN!")
            result(player, dealer)
            game_over = True

        elif cal_value(player) > 21 and cal_value(dealer) > 21:
            print("9) Tie!")
        else:
            print("8) LOSE!")
            game_over = True
            print("Player: ", player, cal_value(player))
            print("Dealer: ", dealer, cal_value(dealer))


