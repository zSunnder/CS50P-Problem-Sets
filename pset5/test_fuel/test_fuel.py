from fuel import convert, gauge
import pytest

def test_fraction():
    assert convert("3/4") == 75
    assert convert("1/4") == 25

def test_zero():
    assert convert("0/1") == 0
    with pytest.raises(ZeroDivisionError):
        convert(1 / 0)
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ZeroDivisionError):
        convert("3/0")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(30) == "30%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"


