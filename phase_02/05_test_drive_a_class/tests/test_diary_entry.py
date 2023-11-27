from lib.diary_entry import *

diary = DiaryEntry("Title", "semper auctor neque vitae tempus")

def test_initialising():
    assert isinstance(diary, DiaryEntry)
    assert diary.title == "Title"
    assert diary.contents == "semper auctor neque vitae tempus"

def test_format():
    assert diary.format() == "Title: semper auctor neque vitae tempus"

def test_count_words():
    assert diary.count_words() == 5

def test_reading_time():
    assert diary.reading_time(1) == 5
    assert diary.reading_time(2) == 2.5
    assert diary.reading_time(5) == 1

def test_reading_chunck():
    assert diary.reading_chunk(2, 1) == "semper auctor"
    assert diary.reading_chunk(2, 1) == "neque vitae"
    assert diary.reading_chunk(2, 1) == "tempus"
    assert diary.reading_chunk(3, 1) == "semper auctor neque"