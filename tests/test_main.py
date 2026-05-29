# test_palindrom.py
import pytest
from palindrom import is_palindrom

def test_palindrom_true():
    assert is_palindrom("madam") == True

def test_palindrom_false():
    assert is_palindrom("hello") == False

def test_palindrom_empty_string():
    assert is_palindrom("") == True

def test_palindrom_single_character():
    assert is_palindrom("a") == True

def test_palindrom_numbers():
    assert is_palindrom("12321") == True

def test_palindrom_mixed_case():
    assert is_palindrom("Madam") == True

def test_palindrom_non_string():
    with pytest.raises(TypeError):
        is_palindrom(123)
