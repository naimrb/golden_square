# tracks.py

## 1. Describe the Problem

As a user\
So that I can keep track of my music listening\
I want to add tracks I've listened to and see a list of them.\

## 2. Design the Function Signature

```python
class Tracks():
    def __init__(self):
    """
    Parameters:
        titles: an empty list

    Returns: 
        nothing
    """
    def add(self, song):
    """
    Parameters:
        song: a string, the title of the song listened to

    Returns: 
        nothing
    """
    def list(self):
    """
    Parameters:
        none
    Returns: 
        self.titles: a list containing all the tracks listened to
    """
```

## 3. Create Examples as Tests


```python
"""
Check initalization of the instance 
"""
track = Tracks()
isinstance(track, Tracks) => True

"""
Given a track add it to the listened tracks 
"""
track.add('My Song')
track.titles => ['My Song']

"""
Calling list() returns a list of all listened tracks 
"""
track.list() => ['My Song']
```