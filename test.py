import math_func

def test_answer():
    assert math_func.func(3) == 4

def test_add():
    assert math_func.add(17, 3) == 20
    assert math_func.add(17) == 19
    assert math_func.add(5) == 7

def test_product():
    assert math_func.product(3, 3) == 9
    assert math_func.product(3) == 6
    assert math_func.product(6) == 12