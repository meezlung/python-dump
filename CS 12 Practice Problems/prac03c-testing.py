from cs12232prac03c import Movements, Point
   
test0 = Movements(Point(1, 2, 3))
test1 = Movements(Point(10, -30, 0))
test2 = Movements(Point(69, 420, 41))

test0.move_to("+x")
test0.move_to("-x")

print(test0.visited_points)
