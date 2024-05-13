from numb3rs import validate

def test_validater():
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("1.2342.2432.432") == False
    assert validate("5342.123.123.123") == False

def test_long():
    assert validate("512.512.512.512.1") == False

