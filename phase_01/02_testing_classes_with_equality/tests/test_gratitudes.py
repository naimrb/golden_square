from lib.gratitudes import *

gratitudes = Gratitudes()

def test_initialising():
    assert isinstance(gratitudes, Gratitudes)
    assert gratitudes.gratitudes == []

def test_add():
    gratitudes.add("Test1")
    assert gratitudes.gratitudes == ['Test1']

    gratitudes.add("Test2")
    assert gratitudes.gratitudes == ['Test1', 'Test2']

def test_format():
    assert gratitudes.format() == "Be grateful for: Test1, Test2"