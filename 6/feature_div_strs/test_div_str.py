import pytest
from div_str import div_str

def test_valid_divisions():
    assert div_str('4', '2') == '2.0'
    assert div_str('1000', '1000') == '1.0'
    assert div_str('-3', '-4') == '0.75'

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        div_str('2', '0')

def test_type_error():
    with pytest.raises(TypeError):
        div_str(3, 3)