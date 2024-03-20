# pyright: strict

from pytest import raises
from cs12232prac05a import Point as Pt
from cs12232prac05a import is_axis_aligned

def test_is_axis_aligned_typical_usage():
    assert is_axis_aligned((Pt(-5, 3), Pt(2, 3), Pt(2, 11), Pt(-5, 11)))
    assert is_axis_aligned((Pt(-5, 11), Pt(2, 11), Pt(2, 3), Pt(-5, 3)))
    assert is_axis_aligned((Pt(-5, 11), Pt(-5, 3), Pt(2, 3), Pt(2, 11)))
    assert is_axis_aligned((Pt(1, 1), Pt(5, 1), Pt(5, 4), Pt(1, 4)))
    assert is_axis_aligned((Pt(-1, -1), Pt(-1, 3), Pt(3, 3), Pt(3, -1)))
    assert is_axis_aligned((Pt(2, 2), Pt(2, 6), Pt(6, 6), Pt(6, 2)))
    assert is_axis_aligned((Pt(-3, -3), Pt(-3, 1), Pt(1, 1), Pt(1, -3)))

    # larger values
    assert is_axis_aligned((Pt(-100, -50), Pt(200, -50), Pt(200, 50), Pt(-100, 50)))
    assert is_axis_aligned((Pt(-20, 10), Pt(30, 10), Pt(30, -20), Pt(-20, -20)))
    assert is_axis_aligned((Pt(-500, 300), Pt(700, 300), Pt(700, 600), Pt(-500, 600)))
    assert is_axis_aligned((Pt(-1000, -500), Pt(2000, -500), Pt(2000, 1000), Pt(-1000, 1000)))
    assert is_axis_aligned((Pt(-1000000, -500000), Pt(2000000, -500000), Pt(2000000, 500000), Pt(-1000000, 500000)))

    assert not is_axis_aligned((Pt(1, 1), Pt(4, 4), Pt(6, 1), Pt(3, -2)))
    assert not is_axis_aligned((Pt(-3, 2), Pt(0, 5), Pt(3, 2), Pt(0, -1)))
    assert not is_axis_aligned((Pt(0, 0), Pt(4, 3), Pt(8, 0), Pt(4, -3)))
    assert not is_axis_aligned((Pt(2, -1), Pt(5, 2), Pt(8, -1), Pt(5, -4)))
    assert not is_axis_aligned((Pt(-5, 3), Pt(-2, 6), Pt(1, 3), Pt(-2, 0)))

    # not aligned properly
    assert not is_axis_aligned((Pt(0, 0), Pt(0, 5), Pt(4, 5), Pt(4, 1)))
    assert not is_axis_aligned((Pt(0, 0), Pt(1, 5), Pt(4, 5), Pt(4, 1)))
    assert not is_axis_aligned((Pt(-1000, -501), Pt(2000, -500), Pt(2000, 1000), Pt(-1000, 1000)))

    # are rectangle coordinates but does not form a rectangle when connected sunod-sunod
    assert not is_axis_aligned((Pt(-5, 11), Pt(2, 11), Pt(-5, 3), Pt(2, 3)))
    assert not is_axis_aligned((Pt(-3, -3), Pt(-3, 1), Pt(1, -3), Pt(1, 1)))
    assert not is_axis_aligned((Pt(-5, 11), Pt(-5, 3), Pt(2, 11), Pt(2, 3)))
    assert not is_axis_aligned((Pt(-3, -3), Pt(1, 1), Pt(-3, 1), Pt(1, -3)))
    assert not is_axis_aligned((Pt(6, 2), Pt(2, 6), Pt(6, 6), Pt(2, 2)))

    

    # squares are rectangles
    assert is_axis_aligned((Pt(0, 0), Pt(0, 1), Pt(1, 1), Pt(1, 0)))
    assert is_axis_aligned((Pt(-2, 1), Pt(3, 1), Pt(3, 6), Pt(-2, 6)))
    assert is_axis_aligned((Pt(0, 0), Pt(5, 0), Pt(5, 5), Pt(0, 5)))
    assert is_axis_aligned((Pt(2, -3), Pt(7, -3), Pt(7, 2), Pt(2, 2)))

    # squares not axis alligned
    assert not is_axis_aligned((Pt(0, 0), Pt(1, 1), Pt(0, 2), Pt(-1, 1)))
    assert not is_axis_aligned((Pt(1, 1), Pt(4, 4), Pt(7, 1), Pt(4, -2)))
    assert not is_axis_aligned((Pt(-2, 3), Pt(1, 6), Pt(4, 3), Pt(1, 0)))
    assert not is_axis_aligned((Pt(0, 0), Pt(3, 3), Pt(6, 0), Pt(3, -3)))
    assert not is_axis_aligned((Pt(-6, 8), Pt(-3, 12), Pt(1, 6), Pt(-2, 2)))
    assert not is_axis_aligned((Pt(2, 5), Pt(5, 8), Pt(8, 5), Pt(5, 2)))



def test_is_axis_aligned_invalid():
    # has duplicate coordinate
    with raises(ValueError):
        is_axis_aligned((Pt(0, 0), Pt(0, 0), Pt(0, 10), Pt(0, 10)))
    with raises(ValueError):
        is_axis_aligned((Pt(0, 0), Pt(5, 10), Pt(5, 10), Pt(10, 0)))
    with raises(ValueError):
        is_axis_aligned((Pt(0, 0), Pt(0, 0)))
    with raises(ValueError):
        is_axis_aligned((Pt(0, 0), Pt(0, 0), Pt(3, 10), Pt(3, 10)))
    with raises(ValueError):
        is_axis_aligned((Pt(0, 0), Pt(0, 0), Pt(0, 0), Pt(0, 0)))
    with raises(ValueError):
        is_axis_aligned(())

    # not a rectangle
    with raises(ValueError):
        is_axis_aligned((Pt(0, 0), Pt(1, 0), Pt(1, 10)))
    with raises(ValueError):
        is_axis_aligned((Pt(0, 0), Pt(3, 10)))
    with raises(ValueError):
        is_axis_aligned((Pt(0, 0), Pt(3, 10), Pt(5, 10)))

    # not a valid representation of a rectangle,
    # even though it looks like a rectangle when drawn
    with raises(ValueError):
        is_axis_aligned((Pt(0, 0), Pt(0, 1), Pt(0, 2), Pt(1, 2), Pt(1, 0)))
    with raises(ValueError):
        is_axis_aligned((Pt(0, 0), Pt(0, 2), Pt(1, 2), Pt(1, 2), Pt(1, 0)))

test_is_axis_aligned_invalid()
test_is_axis_aligned_typical_usage()