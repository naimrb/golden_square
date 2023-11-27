from lib.check_codeword import *

def test_codeword_horse():
    assert check_codeword("horse") == "Correct! Come in."

def test_codeword_close():
    assert check_codeword("hose") == "Close, but nope."

def test_codeword_else():
    assert check_codeword("abc") == "WRONG!"