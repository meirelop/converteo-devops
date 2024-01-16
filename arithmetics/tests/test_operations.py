from arithmetics.operations import add, subtract, multiply


def test_add():
    assert add(5, 3) == 8
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(10, 5, 3) == 2
    assert subtract(5, 3, 2) == 0
    assert subtract(-3, -2, -1) == 0


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-1, 5) == -5
    assert multiply(0, 10) == 0
