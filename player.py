
class Player:
    def __init__(self, name="new_player", money=100, rank_only=True, strategy="H17", betting_strategy="ask"):
        self.name = name
        self.money = money
        self.bet_amount = 0
        self.hand = []
        self.rank_only = rank_only
        self.strategy = strategy
        self.betting_strategy = betting_strategy
    def __str__(self):
        return "{:8.8} -> Money: {:5} betting : {:5} Down: {:5} Hit: {} Hand: {}".format(
            self.name, self.money, self.betting_strategy, self.bet_amount, self.rank_only, self.hand)

    def __repr__(self):
        return self.name


def main():
    p1 = Player("12345676890")
    p2 = Player("p2")
    p3 = Player("p3")
    p4 = Player("p4")
    p1.money = 10
    p2.money = 20
    print(p1)
    print(p2)
    pees = [p1, p2, p3, p4]
    for p in pees:
        print("\t", p)
    print(pees)


if __name__ == '__main__':
    main()
