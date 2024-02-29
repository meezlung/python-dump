from cs12232prac03c import Point, Movements

m = Movements(Point(10, -30, 0))

m.move_to('+x')
m.move_to('+z')
m.move_to('+z')
m.move_to('-z')
m.move_to('-y')
m.teleport_to(Point(100, 100, 100))


assert m.visited_count() == 6

assert m.visited() == {
    Point(100, 100, 100),
    Point(10, -30, 0),
    Point(11, -30, 0),
    Point(11, -30, 1),
    Point(11, -30, 2),
    Point(11, -31, 1),
}