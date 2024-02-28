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

        self.visited_points: set[Point] = set()
        self.visited_points.add(point)

    def move_to(self, dir: str) -> None: 
        x, y, z = self.x, self.y, self.z
        if dir == "+x":
            x += 1
        if dir == "-x":
            x -= 1
        if dir == "+y":
            y += 1
        if dir == "-y":
            y -= 1
        if dir == "+z":
            z += 1
        if dir == "-z":
            z -= 1
        else:
            return None
        
        new_point = Point(x, y, z)
        self.x, self.y, self.z = new_point
        self.visited_points.add(new_point)
        
    def teleport_to(self, point: Point) -> None:
        self.x, self.y, self.z = point.x, point.y, point.z
        self.visited_points.add(point)

    def visited(self) -> set[Point]:
        return self.visited_points
    
    def visited_count(self) -> int:
        return len(self.visited_points)