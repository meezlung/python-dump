from typing import Sequence, TypeVar

T = TypeVar('T')

def stack_like_pancakes(l: Sequence[list[T]]) -> list[T]:
    stack: list[T] = []

    for elem in l:
        for e in reversed(elem):
            stack.append(e)
    
    return stack 