from lib.grammar_stats import *

stats = GrammarStats()

def test_grammar_check():
    assert stats.check("Test.") == True
    assert stats.check("my name is Naim.") == False

def test_grammar_percentage():
    assert stats.percentage_good() == 50
    stats.check("Test.")
    stats.check("Test.")
    assert stats.percentage_good() == 75