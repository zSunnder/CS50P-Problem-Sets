from bank import value

def test_hello():
    assert value("HELLO") == 0
    assert value("hello, david") == 0
    assert value("hello, friend") == 0

def test_h():
    assert value("hi") == 20
    assert value("hola, david") == 20
    assert value("hey") == 20

def test_noH():
    assert value("amigo") == 100
    assert value("xopa") == 100
    assert value("fren") == 100

