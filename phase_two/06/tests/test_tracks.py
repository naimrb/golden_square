from lib.tracks import *

track = Tracks()

def test_initalising():
    assert isinstance(track, Tracks)
    assert track.titles == []

def test_tracks_add():
    track.add('My Song 1')
    assert track.titles == ['My Song 1']

    track.add('My Song 2')
    assert track.titles == ['My Song 1', 'My Song 2']

def test_tracks_list():
    assert track.list() == ['My Song 1', 'My Song 2']