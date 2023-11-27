from lib.string_builder import *

builder = StringBuilder()

def test_initialising():
    assert isinstance(builder, StringBuilder)
    assert builder.str == ""

def test_add():
    builder.add("abc")
    assert builder.str == "abc"

    builder.add("def")
    assert builder.str == "abcdef"

def test_size():
    #str = "abcdef" (6)
    assert builder.size() == 6

def test_output():
    assert builder.output() == "abcdef"