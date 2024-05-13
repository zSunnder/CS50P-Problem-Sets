from seasons import Time
from datetime import date
import pytest
import inflect


def test_valid():
    today = date.today()
    birth = date(2000, 7, 31)
    p = inflect.engine()
    time = today - birth
    minutes = int(time.days)*24*60
    words = p.number_to_words(minutes, andword="").capitalize()
    result = f"{words} minutes"

    assert result == "Twelve million, four hundred ninety-three thousand, four hundred forty minutes"


