from lib.diary import *
from lib.diary_entry import *

words = "sed tempus urna et pharetra pharetra massa massa ultricies mi"

entry1 = DiaryEntry("Test1", words)
entry2 = DiaryEntry("Test2", words)
entry3 = DiaryEntry("Test3", "sed tempus urna et")

diary = Diary()

def test_initialising():
    assert isinstance(diary, Diary)
    assert isinstance(entry1, DiaryEntry)
    assert isinstance(entry2, DiaryEntry)

    assert diary.entries == []

def test_diary_add():
    diary.add(entry1)
    diary.add(entry2)
    assert diary.entries == [entry1, entry2]

def test_diary_list():
    assert diary.all() == [entry1, entry2]

def test_diary_count_words():
    assert diary.count_words() == 20

def test_diary_reading_time():
    assert diary.reading_time(2) == 10
    assert diary.reading_time(5) == 4

def test_diary_find_best_entry_for_reading_time():
    diary.add(entry3)
    assert diary.find_best_entry_for_reading_time(2, 2) == entry3
    assert diary.find_best_entry_for_reading_time(2, 5) == entry1
