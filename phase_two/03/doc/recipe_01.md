# reading_time.py

## 1. Describe the Problem
_As a user\
So that I can manage my time\
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute._

## 2. Design the Function Signature

```python
def reading_time(text):
    """
    Parameters:
        text: a string containing a text

    Returns:
        a float (the reading time in minutes)

    """
```

## 3. Create Examples as Tests


```python
"""
Given a text of 200 words the function will return 1 (the reading time) 
"""
reading_time("200 WORDS...") => 1

"""
Given a text of 2 words the function will return 0.01 (the reading time) 
"""
reading_time("2 WORDS...") => 0.01
```