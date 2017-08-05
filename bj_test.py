from blackjack import cal_all_value
from blackjack import is_soft
from card import Card

test_hand1 = [Card('2', 'S'),
              Card('A', 'C'),
              Card('A', 'D'),
              Card('A', 'S'),
              Card('A', 'H')]
result = cal_all_value(test_hand1)
assert result == [6, 16]
assert is_soft(test_hand1) is True

test_hand2 = [Card('10', 'S'),
              Card('4', 'C'),
              Card('A', 'D'),
              Card('A', 'S'),
              Card('A', 'H')]

assert cal_all_value(test_hand2) == [17]
assert is_soft(test_hand2) is False
