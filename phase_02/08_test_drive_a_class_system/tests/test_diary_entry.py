from lib.diary_entry import *

content = "accumsan tortor posuere ac ut consequat semper viverra nam libero"
title = "Title"
entry = DiaryEntry(title, content)

def test_intialising():
    assert isinstance(entry, DiaryEntry)
    assert entry.title == title
    assert entry.contents == content

def test_count_words():
    assert entry.count_words() == 10

def test_reading_time():
    assert entry.reading_time(2) == 5
    assert entry.reading_time(10) == 1

def test_reading_chunck():
    assert entry.reading_chunk(2, 1) == "accumsan tortor"
    assert entry.reading_chunk(2, 1) == "posuere ac"
    assert entry.reading_chunk(10, 1) == "ut consequat semper viverra nam libero"
    assert entry.reading_chunk(2, 1) == "accumsan tortor"