
class Player:
    def __init__(self, name):
        self.name = name
        self.money = 100
        self.bet_amount = 0
        self.hand = []
        self.rank_only = True
    def __str__(self):
        return "{:8.8} -> Money: {:5} Down: {:5} Hand: {}".format(self.name, self.money, self.bet_amount, self.hand)

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
