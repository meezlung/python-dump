# pyright: strict

from pytest import raises
from cs12232prac05a import Point as Pt
from cs12232prac05a import is_axis_aligned


def test_is_axis_aligned_typical_usage():
    assert is_axis_aligned((Pt(-5, 3), Pt(2, 3), Pt(2, 11), Pt(-5, 11)))
    assert is_axis_aligned((Pt(-5, 11), Pt(2, 11), Pt(2, 3), Pt(-5, 3)))
    assert is_axis_aligned((Pt(-5, 11), Pt(-5, 3), Pt(2, 3), Pt(2, 11)))

    assert not is_axis_aligned((Pt(0, 0), Pt(0, 5), Pt(4, 5), Pt(4, 1)))
    assert not is_axis_aligned((Pt(-5, 11), Pt(2, 11), Pt(-5, 3), Pt(2, 3)))
    assert not is_axis_aligned((Pt(0, 0), Pt(0, 5), Pt(4, 6), Pt(4, 1)))

    # squares are rectangles
    assert is_axis_aligned((Pt(0, 0), Pt(0, 1), Pt(1, 1), Pt(1, 0)))
    assert not is_axis_aligned((Pt(0, 0), Pt(1, 1), Pt(0, 2), Pt(-1, 1)))

def test_is_axis_aligned_invalid():
    # has duplicate coordinate
    with raises(ValueError):
        is_axis_aligned((Pt(0, 0), Pt(0, 0), Pt(0, 10), Pt(0, 10)))
    with raises(ValueError):
        is_axis_aligned((Pt(0, 0), Pt(5, 10), Pt(5, 10), Pt(10, 0)))

    # just a line
    with raises(ValueError):
        is_axis_aligned((Pt(0, 0), Pt(2, 0), Pt(1, 0), Pt(4, 0)))
    with raises(ValueError):
        is_axis_aligned((Pt(0, 0), Pt(0, 2), Pt(0, 5), Pt(0, 1)))


    # not a rectangle
    with raises(ValueError):
        is_axis_aligned((Pt(0, 0), Pt(1, 0), Pt(1, 10)))

    # not a valid representation of a rectangle,
    # even though it looks like a rectangle when drawn
    with raises(ValueError):
        is_axis_aligned((Pt(0, 0), Pt(0, 1), Pt(0, 2), Pt(1, 2), Pt(1, 0)))
    with raises(ValueError):
        is_axis_aligned((Pt(0, 0), Pt(0, 2), Pt(1, 2), Pt(1, 2), Pt(1, 0)))

test_is_axis_aligned_typical_usage()
test_is_axis_aligned_invalid()