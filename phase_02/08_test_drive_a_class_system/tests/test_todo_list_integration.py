from lib.todo_list import *
from lib.todo import *

todo_list = TodoList()
todo1 = Todo("Cleaning")
todo2 = Todo("Laundry")

def test_initialising():
    assert isinstance(todo_list, TodoList)
    assert isinstance(todo1, Todo)
    assert isinstance(todo2, Todo)

def test_todo_list_add():
    todo_list.add(todo1)
    todo_list.add(todo2)

    assert todo_list.todos == [todo1, todo2]

def test_todo_list_incomplete():
    assert todo_list.incomplete() == [todo1, todo2]

def test_todo_list_complete():
    todo2.mark_complete()
    assert todo_list.complete() == [todo2]

def test_todo_list_give_up():
    todo_list.give_up()
    assert todo_list.complete() == [todo1, todo2]