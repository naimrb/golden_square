from lib.greet import *

def test_greet():
    name = "Naim"
    assert greet(name) == f"Hello, {name}!"