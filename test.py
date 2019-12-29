import math_func
import pytest
import sys
def test_answer():
    assert math_func.func(3) == 4

#@pytest.mark.skip(reason ="skipping the test_add function")
#@pytest.mark.number
@pytest.mark.skipif(sys.version_info < (3, 3), reason ="skipping the test_add function")
def test_add():
    assert math_func.add(17, 3) == 20
    assert math_func.add(17) == 19
    assert math_func.add(5) == 7
    print(math_func.add(17, 3),'*************************')


#@pytest.mark.number
def test_product():
    assert math_func.product(3, 3) == 9
    assert math_func.product(3) == 6
    assert math_func.product(6) == 12

#@pytest.mark.strings
def test_add_strings():
    outcome = math_func.add('Namaste', 'Boomidevi')
    assert outcome == 'NamasteBoomidevi'
    assert type(outcome) is str
    assert 'Namaste' in outcome

#@pytest.mark.strings
def test_prodstrings():
    assert math_func.product('Namaste', 3) == 'Namaste' 'Namaste' 'Namaste'
    outcome = math_func.product('Namaste')
    assert outcome == 'NamasteNamaste'
    assert type(outcome) is str
    assert 'Namaste' in outcome

