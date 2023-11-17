from lib.todo import *

def test_todo_task_true():
    assert todo_task("Cleaning #TODO") == True

def test_todo_task_false():
    assert todo_task("Cleaning") == False