import pytest

from cs12232prac04d import MinReadyArray

def test_MinReadyArray():
    # make two instances
    arr1 = MinReadyArray()
    arr2 = MinReadyArray()

    # perform operations
    arr1.append_left(40)
    arr1.append_right(30)
    assert arr1[1] == 30

    # check IndexErrors
    with pytest.raises(IndexError):
        arr1[-1]
    with pytest.raises(IndexError):
        arr2[0]
    with pytest.raises(IndexError):
        arr2.min(-100, 100)

    arr1.append_left(20)
    assert arr1.min(1, 3) == 30
    assert arr1.min(0, 3) == 20
    arr2.append_left(10)
    arr2.append_right(10)
    assert arr2.min(-100, 100) == 10
    assert len(arr1) == 3
    res: int = arr1.pop_left()
    assert res == 20
    assert len(arr1) == 2
