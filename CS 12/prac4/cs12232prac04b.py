from typing import Sequence, TypeVar

T = TypeVar("T")

def swap_pairs(l: Sequence[T]) -> list[T] | None:
    if len(l) % 2 != 0:
        raise ValueError
    
    new_list: list[T] = []

    for x in range(0, len(l), 2):
        new_list.append(l[x + 1])
        new_list.append(l[x])

    return new_list