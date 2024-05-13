from twttr import shorten


def test_wthstring():
    assert shorten("hello") == "hll"
    assert shorten("hola") == "hl"
    assert shorten("QUeSo") == "QS"

def test_nothing():
    assert shorten(" ") == " "
    assert shorten("hjklgfds") == "hjklgfds"

def test_number():
    assert shorten("hello123") == "hll123"
    assert shorten("123455") == "123455"
    assert shorten("he3llo0") == "h3ll0"

def test_puntuation():
    assert shorten("hello, david.") == "hll, dvd."
