from lib.present import *
import pytest

present = Present()

def test_initialising():
    assert isinstance(present, Present)
    assert present.contents == None

def test_unwrap_exception():
    with pytest.raises(Exception) as e:
        present.unwrap()
    
    assert str(e.value) == "No contents have been wrapped."

def test_wrap_exception():
    present.contents = "Bike"
    with pytest.raises(Exception) as e:
        present.wrap("Ball")
    
    assert str(e.value) == "A contents has already been wrapped."