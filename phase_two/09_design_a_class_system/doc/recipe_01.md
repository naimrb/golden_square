## 1. Describe the Problem

As a user\
So that I can record my experiences\
I want to keep a regular diary

As a user\
So that I can reflect on my experiences\
I want to read my past diary entries

As a user\
So that I can reflect on my experiences in my busy day\
I want to select diary entries to read based on how much time I have and my reading speed

As a user\
So that I can keep track of my tasks\
I want to keep a todo list along with my diary

As a user\
So that I can keep track of my contacts\
I want to see a list of all of the mobile phone numbers in all my diary entries

## 2. Design the Function Signature

```python
class Diary()

class Entry()
class Task()
class Contact()

Entry -> Diary
Todo-> Diary
Contact -> Entry -> Diary
```

```python
#lib/diary.py

class Diary():
    # Public properties:
    #   entries:  a list of Entry instances
    #   contacts: a list of Contact instances
    #   todos:    a list of Todos instances
    
    def __init__(self):
    """
    Parameters:
        none
    Returns: 
        nothing
    Side-effects:
        sets the entries, contacts and todos properties to an empty list
    """
    def add(self, instance):
    """
    Parameters:
        instance: an instance of Entry, Todo or Contact
    Returns:
        nothing
    """
    def list(self, data):
    """
    Parameters:
        data: a string, the type of data to return ('entries', 'todos', 'contacts')
    Returns: 
        a list of the specified instances
    """
    def best_entry_for_time(self, wpm, min):
    """
    Parameters:
        wpm: an integer, words per minutes
        min: an integer, the amount of minutes
    Returns: 
        an element of entries
    """
```
```python
#lib/entry.py

class Entry():
    # Public properties:
    #   title:  a string
    #   content: a string

    def __init__(self, title, content):
    """
    Parameters:
        title: a string, indicating the title
        content: a string, indicating the content
    Returns: 
        nothing
    Side-effects:
        sets the title and content properties
    """
    def count_words(self):
    """
    Parameters:
        none
    Returns:
        the number of words from the entry
    """
    def parse_phone_number(self):
    """
    Parameters:
        none
    Returns:
        the first phone number if the contents contains one
    """
```
```python
#lib/contact.py

class Contact():
    # Public properties:
    #   entry:   an instance, of entry
    #   number: a string, parsed phone number

    def __init__(self, entry, number):
    """
    Parameters:
        entry: an instance
        number: a string
    Returns: 
        nothing
    Side-effects:
        sets the entry and number properties
    """
```
```python
#lib/task.py

class Task():
    # Public properties:
    #   name:   a string, name of the task
    #   status: a boolean, True if completed False if not (False by default)

    def __init__(self, name):
    """
    Parameters:
        name: a string
    Returns: 
        nothing
    Side-effects:
        sets the name and status properties
    """
    def completed(self):
    """
    Parameters:
        none
    Returns:
        nothing
    Side-effects:
        sets the status property to True
    """
```

## 3. Create Examples as Tests


```python
"""
Check initalization of the instance 
"""


```