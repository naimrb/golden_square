from lib.report_length import *

def test_length_one():
    length = 1
    assert report_length("a") == f"This string was {length} characters long."

def test_length_three():
    length = 3
    assert report_length("abc") == f"This string was {length} characters long."