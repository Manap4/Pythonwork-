import pytest
from fuel import convert, gauge

# test cases for convert
def test_convert_valid_input():
    assert convert('3/4') == 75
    assert convert('1/2') == 50

def test_convert_invalid_input():
    with pytest.raises(ValueError):
        convert('1/0')
    with pytest.raises(ValueError):
        convert('2.5/3')
    with pytest.raises(ValueError):
        convert('3/2.5')

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_convert_rounding():
    assert convert('1/3') == 33
    assert convert('2/3') == 67
    assert convert('1/7') == 14

# test cases for gauge
def test_gauge_edge_cases():
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'

def test_gauge_other_cases():
    assert gauge(42) == '42%'
    assert gauge(75) == '75%'
    assert gauge(50) == '50%'

