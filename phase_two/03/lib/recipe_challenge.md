# todo.py

## 1. Describe the Problem
As a user\
So that I can keep track of my tasks\
I want to check if a text includes the string #TODO.

## 2. Design the Function Signature

```python
def todo_tasks(text):
    """
    Parameters:
        text: a string containing a text

    Returns:
        a boolean (True if it contains #TODO, False if not)

    """
```

## 3. Create Examples as Tests


```python
"""
Given a text the function will return a boolean True if it contains #TODO, if not False. 
"""
todo_task("Cleaning") => False
todo_task("Cleaning #TODO") => True