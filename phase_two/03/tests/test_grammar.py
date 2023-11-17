from lib.grammar import *

def test_grammar():
    assert grammar("hello my name is Naim") == "Hello my name is Naim."