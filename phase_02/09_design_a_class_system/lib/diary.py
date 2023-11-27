from lib.entry import *
from lib.task import *
from lib.contact import *

class Diary():
    # Public properties:
    #   entries:  a list of Entry instances
    #   contacts: a list of Contact instances
    #   todos:    a list of Todos instances
    
    def __init__(self):
        self.entries = []
        self.contacts = []
        self.todos = []

    def add(self, instance):
        if type(instance) == Entry:
            self.entries.append(instance)
            contact_number = instance.parse_phone_number()
            
            if contact_number != None:
                contact = Contact(instance, contact_number)
                self.contacts.append(contact)

        elif type(instance) == Task:
            self.todos.append(instance)

    def list(self, data):
        if data == "entries":
            return self.entries
        
        elif data == "todos":
            return self.todos
        
        elif data == "contacts":
            return self.contacts

    def best_entry_for_time(self, wpm, min):
        readable_words = wpm * min
        best_entry_words = 0
        best_entry = None

        for e in self.entries:
            e_words = e.count_words()
            if e_words <= readable_words and e_words > best_entry_words:
                best_entry_words = e_words
                best_entry = e 
        
        return best_entry

