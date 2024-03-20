from typing import Sequence
from collections import Counter

def first_digits(data: Sequence[int]) -> Counter[int]:
    filtered: list[int] = []

    for number in data:
        if number < 0:
            raise ValueError
        filtered.append(int(str(number)[0]))

    return Counter(filtered)