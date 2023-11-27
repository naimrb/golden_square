from lib.entry import *
from lib.contact import *
from lib.diary import *
from lib.task import *

diary = Diary()

e1 = Entry("Entry 1", "quis commodo odio aenean sed adipiscing diam donec adipiscing tristique")
e2 = Entry("Entry 2", "lectus arcu 07456249865 bibendum at varius vel")
e3 = Entry("Entry 3", "lectus arcu bibendum 07 54 62 54 56 9 at")

t1 = Task("Clean")
t2 = Task("Washing")

def test_initialising():
    assert isinstance(diary, Diary)
    assert diary.entries == []
    assert diary.contacts == []
    assert diary.todos == []

def test_diary_add_entry():
    diary.add(e1)
    assert diary.entries[0].title == "Entry 1"
    
    diary.add(e2)
    diary.add(e3)
    assert diary.entries == [e1, e2, e3]

def test_diary_add_contact():
    assert len(diary.contacts) == 2 # type: ignore
    assert diary.contacts[0].number == "07456249865"
    assert diary.contacts[1].number == "07546254569"
    assert diary.contacts[0].entry == e2

def test_diary_add_todo():
    diary.add(t1)
    assert diary.todos[0].name == "Clean"
    assert len(diary.todos) == 1

    diary.add(t2)
    assert diary.todos == [t1, t2]

def test_diary_list_entry():
    assert diary.list("entries") == [e1, e2, e3]

def test_diary_list_contact():
    contacts = diary.list("contacts")
    assert contacts[0].number == "07456249865"
    assert contacts[1].number == "07546254569"
    assert len(contacts) == 2

def test_diary_list_todo():
    todos = diary.list("todos")
    assert len(todos) == 2
    assert todos[1].name == "Washing"
    assert todos == [t1, t2]

def test_diary_best_entry():
    assert diary.best_entry_for_time(4, 2) == e2
    assert diary.best_entry_for_time(4, 3) == e1