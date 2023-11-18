from lib.tasks import *

tracker = TaskTracker()

def test_initalising():
    assert isinstance(tracker, TaskTracker)
    assert tracker.tasks == []

def test_tasks_add():
    tracker.add('Cleaning')
    tracker.add('Laundry')
    assert tracker.tasks == ['Cleaning', 'Laundry']

def test_tasks_list():
    assert tracker.list() == ['Cleaning', 'Laundry']

def test_tasks_completed():
    tracker.completed('Cleaning')
    assert tracker.tasks == ['Laundry']
    
    tracker.completed('Laundry')
    assert tracker.tasks == []