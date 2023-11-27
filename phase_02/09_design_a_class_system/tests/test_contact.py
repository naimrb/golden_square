from lib.contact import *
from lib.entry import *

e = Entry("Entry 1", "lectus arcu 07456249865 bibendum at varius vel")
c = Contact(e, "07856452714")

def test_initialising():
    assert isinstance(c, Contact)
    assert c.entry == e
    assert c.number == "07856452714"