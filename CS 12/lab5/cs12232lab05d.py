from typing import Sequence

class Pusher:
    def __init__(self, grid: Sequence[str], pepe: tuple[int, int], box: tuple[int, int]) -> None:
        self.warehouse_floor = grid
        self.pepe = pepe
        self.box = box

    def move(self, dir: str) -> bool:
        temp_pepe: tuple[int, int] = (0, 0)
        if dir == "R":
            temp_pepe = (self.pepe[0] + 1, self.pepe[1])
        elif dir == "L":
            temp_pepe = (self.pepe[0] - 1, self.pepe[1])
        elif dir == "U":
            temp_pepe = (self.pepe[0], self.pepe[1] - 1)
        elif dir == "D":
            temp_pepe = (self.pepe[0], self.pepe[1] + 1)

        if temp_pepe != self.pepe:
            return True
        return False
    
    def push(self, dir: str) -> bool:
        pass