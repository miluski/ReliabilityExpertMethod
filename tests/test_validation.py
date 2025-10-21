import pytest
from src.utils.data_validation import validate_positive_number, validate_percentage

def test_validate_positive_number_valid():
    """Test walidacji liczby dodatniej - przypadek poprawny"""
    result = validate_positive_number(5.5)
    assert result == 5.5

def test_validate_positive_number_string():
    """Test walidacji liczby dodatniej z stringa"""
    result = validate_positive_number("10.5")
    assert result == 10.5

def test_validate_positive_number_zero():
    """Test walidacji zera - powinien rzucić wyjątek"""
    with pytest.raises(ValueError):
        validate_positive_number(0)

def test_validate_positive_number_negative():
    """Test walidacji liczby ujemnej - powinien rzucić wyjątek"""
    with pytest.raises(ValueError):
        validate_positive_number(-5)

def test_validate_percentage_valid():
    """Test walidacji procentu - przypadek poprawny"""
    result = validate_percentage(50.5)
    assert result == 50.5

def test_validate_percentage_zero():
    """Test walidacji procentu - zero jest poprawne"""
    result = validate_percentage(0)
    assert result == 0

def test_validate_percentage_hundred():
    """Test walidacji procentu - 100 jest poprawne"""
    result = validate_percentage(100)
    assert result == 100

def test_validate_percentage_over_hundred():
    """Test walidacji procentu > 100 - powinien rzucić wyjątek"""
    with pytest.raises(ValueError):
        validate_percentage(101)

def test_validate_percentage_negative():
    """Test walidacji procentu ujemnego - powinien rzucić wyjątek"""
    with pytest.raises(ValueError):
        validate_percentage(-10)
