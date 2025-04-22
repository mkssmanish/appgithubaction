from src.math_operations import add, sub, mul



def test_add():
    assert add(2,3) == 6
    assert add(2,8) == 10
    


def test_sub():
    assert sub(5,3) == 2
    assert sub(5,5) == 0
    assert sub (2,5) == -3


def test_mul():
    assert mul(5,2) == 10
    assert mul(5,0) == 0
    assert mul(0, 0) == 0
    assert mul(5,5) == 25


test_add()
test_sub()
test_mul()
