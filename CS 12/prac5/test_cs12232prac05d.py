# pyright: strict

from pytest import raises
from cs12232prac05d import BiDict

def test_BiDict():
    b = BiDict[str, int]({
            'poe': 3,
            'e': 1,
            'near': 4,
            'a': 1,
            'raven': 5,
            'midnights': 9,
            'so': 2,
            'dreary': 6,
            'tired': 5,
            'and': 3,
            'weary': 5,
        })

    assert b['e'] == 1
    assert b.keys_with_value(1) == {'a', 'e'}
    assert b.keys_with_value(8) == set()
    assert len(b) == 11

    b['silently'] = 8

    assert b.keys_with_value(8) == {'silently'}
    assert len(b) == 12

    res: int = b.pop('silently')

    assert res == 8
    assert b.keys_with_value(8) == set()
    assert len(b) == 11

    b['a'] = -1

    assert len(b) == 11

    with raises(KeyError):
        b['test'] 
    with raises(KeyError):
        b.pop('test')

test_BiDict()