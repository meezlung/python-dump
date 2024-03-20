from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int
    z: int

class Movements:
    def __init__(self, point: Point) -> None:
        self.x: int = point.x
        self.y: int = point.y
        self.z: int = point.z

        self.visited_points: set[Point] = {point}
        self.visited_points.add(point)

    def move_to(self, dir: str) -> None: 
        if dir == "+x":
            self.x += 1
        if dir == "-x":
            self.x -= 1
        if dir == "+y":
            self.y += 1
        if dir == "-y":
            self.y -= 1
        if dir == "+z":
            self.z += 1
        if dir == "-z":
            self.z -= 1

        new_point = Point(self.x, self.y, self.z)
        self.visited_points.add(new_point)

    def teleport_to(self, point: Point) -> None:
        self.x, self.y, self.z = point.x, point.y, point.z
        self.visited_points.add(point)

    def visited(self) -> set[Point]:
        return self.visited_points
    
    def visited_count(self) -> int:
        return len(self.visited_points)