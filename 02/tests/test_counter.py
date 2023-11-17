from lib.counter import *

counter = Counter()

def test_initialising():
    assert isinstance(counter, Counter)
    assert counter.count == 0

def test_add():
    counter.add(1)
    assert counter.count == 1
    
    counter.add(2)
    assert counter.count == 3

def test_report():
    count = 3
    assert counter.report() == f"Counted to {count} so far."