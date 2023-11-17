# grammar.py

## 1. Describe the Problem
As a user\
So that I can improve my grammar\
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

```python
def grammar(text):
    """
    Parameters:
        text: a string containing a text

    Returns:
        a string (the formatted text)

    """
```

## 3. Create Examples as Tests


```python
"""
Given a text the function will return a formatted result starting with a capital
letter and ending with a punctuation. 
"""
grammar("hello my name is Naim") => "Hello my name is Naim."