from src.math_operations import add, sub



def test_add():
    assert add(2,3) == 5
    assert add(2,8) == 10
    


def test_sub():
    assert sub(5,3) == 2
    assert sub(5,5) == 0
    assert sub (2,5) == -3