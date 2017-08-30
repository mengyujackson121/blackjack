
class Player:
    def __init__(self, name="new_player", money=100, rank_only=True,
                 strategy="H17", betting_strategy="ask", tie_behavior="dealer_wins",
                 blackjack_multiplier=0.5, bet_amount=0):
        self.name = name
        self.money = money
        self.bet_amount = bet_amount
        self.hand = []
        self.rank_only = rank_only
        self.strategy = strategy
        self.betting_strategy = betting_strategy
        self.tie_behavior = tie_behavior
        self.blackjack_multiplier = blackjack_multiplier

    def __str__(self):
        return "{:8.8} -> Money: {:5} betting : {:5} Down: {:5} Hit: {} Hand: {}".format(
            self.name, self.money, self.betting_strategy, self.bet_amount, self.rank_only, self.hand)

    def __repr__(self):
        return self.name