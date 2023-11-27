from lib.diary import *

def test_make_snippet_five_words():
    assert make_snippet("T1 T2 T3 T4 T5") == "T1 T2 T3 T4 T5"

def test_make_snippet_more_than_five_words():
    assert make_snippet("T1 T2 T3 T4 T5 T6") == "T1 T2 T3 T4 T5..."

def test_count_words():
    assert count_words("T1 T2 T3") == 3
    assert count_words("T1 T2") == 2