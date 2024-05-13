import pytest
from unittest.mock import patch
from project import Money
from project import Blackjack

def test_depopsit():
    money = Money()
    money.deposit(100)
    assert str(money) == "100"
    money.withdraw(50)
    assert str(money) == "50"

def test_withdraw():
    money = Money()
    money.deposit(100)
    money.withdraw(50)
    assert str(money) == "50"

def test_blackjack():
    blackjack = Blackjack()
    hand = ["10♠", "A♡"]
    assert blackjack.calculate(hand) == 21

def test_game():
    blackjack = Blackjack()
    with patch("builtins.input", side_effect=["stand"]):
        assert blackjack.game() is False
