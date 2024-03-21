from typing import Sequence
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

def has_conflict(p: Sequence[Point], f: Sequence[Point]) -> bool:
    def is_axis_aligned(polygon: Sequence[Point]) -> bool:
        p1, p2, p3, p4 = polygon
        
        trues = 0

        if len(polygon) != 4 or (p1 == p2 or p3 == p4 or p1 == p3 or p2 == p4 or p1 == p4 or p2 == p3) or (p1.x == p2.x == p3.x == p4.x or p1.y == p2.y == p3.y == p4.y):
            raise ValueError

        for i in range(len(polygon)):
            if i == 3:
                if polygon[i].x == polygon[0].x or polygon[i].y == polygon[0].y:
                    trues += 1
            else:
                if polygon[i].x == polygon[i + 1].x or polygon[i].y == polygon[i + 1].y:
                    trues += 1

        return True if trues == 4 else False
    
    if is_axis_aligned(p) and is_axis_aligned(f):
        p1, p2, p3, p4 = p

        for f_i in f:
            if min(p1.x, p2.x, p3.x, p4.x) <= f_i.x <= max(p1.x, p2.x, p3.x, p4.x) and min(p1.y, p2.y, p3.y, p4.y) <= f_i.y <= max(p1.y, p2.y, p3.y, p4.y):
                return True
            
        return False
    
    else:
        raise ValueError