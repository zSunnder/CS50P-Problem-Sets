from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(113)
    jar.deposit(3)
    assert jar.size == 3



def test_withdraw():
    jar = Jar()
    jar.deposit(2)
    jar.withdraw(1)
    assert str(jar) == "🍪"
    jar.deposit(4)
    jar.withdraw(2)
    assert str(jar) == "🍪🍪🍪"
    jar.deposit(9)
    jar.withdraw(5)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪"
