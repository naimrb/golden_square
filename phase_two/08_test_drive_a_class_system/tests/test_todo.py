from lib.todo import *

task = Todo("Clean")

def test_initialising():
    assert isinstance(task, Todo)
    assert task.complete == False
    assert task.task == "Clean"

def test_mark_complete():
    task.mark_complete()
    assert task.complete == True