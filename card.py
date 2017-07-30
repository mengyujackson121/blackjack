class Card():
    long_rank = {
        "A": "Ace",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
        "10": "Ten",
        "J": "Jack",
        "Q": "Queen",
        "K": "King"
    }

    long_suit = {
        "C": "Clubs",
        "D": "Diamonds",
        "H": "Hearts",
        "S": "Spades"
    }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + self.suit

    def long(self, rank_only=False):
        string = Card.long_rank[self.rank]

        if not rank_only:
            string += " of " + Card.long_suit[self.suit]

        return string


def main():
    import random
    deck = [Card(rank, suit)
            for rank in ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
            for suit in ("C", "D", "H", "S")]
    random.shuffle(deck)
    for count, card in enumerate(deck):
        if count % 4 == 0:
            print(card)
        elif count % 4 == 1:
            print(card.rank)
        elif count % 4 == 2:
            print(card.long())
        elif count % 4 == 3:
            print(card.long(rank_only=True))


def standard_deck():
    return [Card(rank, suit)
            for rank in ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
            for suit in ("C", "D", "H", "S")]


if __name__ == "__main__":
    main()
