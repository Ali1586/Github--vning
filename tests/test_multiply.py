

def test_multiply():
    a = 4
    b = 6
    print(a *b)
    assert 4 * 6 == 24

def test_med_zero():
    a = 4
    b = 0
    print(a * b)
    assert 4 * 0 == 0

def test_med_negative():
    a = -2
    b = 4
    print(a * b)
    assert -2 * 4 == -8
