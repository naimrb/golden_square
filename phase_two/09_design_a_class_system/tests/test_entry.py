from lib.entry import *

e = Entry("Entry 1", "lectus arcu 07456249865 bibendum at varius vel")

def test_initialising():
    assert isinstance(e, Entry)
    assert e.title == "Entry 1"
    assert e.content == "lectus arcu 07456249865 bibendum at varius vel"

def test_count_words():
    assert e.count_words() == 7

    e.content = "lectus arcu 07456249865 bibendum at varius"
    assert e.count_words() == 6

def test_parse_phone_number():
    assert e.parse_phone_number() == "07456249865"
    
    e.content = "lectus arcu bibendum at varius"
    assert e.parse_phone_number() == None

    e.content = "lectus arcu bibendum at varius 0754681"
    assert e.parse_phone_number() == None

    e.content = "lectus arcu bibendum at varius 0 78 54 21 36 52"
    assert e.parse_phone_number() == "07854213652"