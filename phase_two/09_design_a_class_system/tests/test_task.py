from lib.task import *

t = Task("Clean")

def test_initialising():
    assert isinstance(t, Task)
    assert t.name == "Clean"
    assert t.status == False

def test_completed():
    assert t.status == False
    
    t.completed()
    assert t.status == True