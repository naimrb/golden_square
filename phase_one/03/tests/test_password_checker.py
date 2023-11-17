from lib.password_checker import *
import pytest

checker = PasswordChecker()

def test_initialising():
    assert isinstance(checker, PasswordChecker)

def test_check():
    assert checker.check("12345678") == True

def test_check_exception():
    with pytest.raises(Exception) as e:
        checker.check("123")

    assert str(e.value) == "Invalid password, must be 8+ characters."