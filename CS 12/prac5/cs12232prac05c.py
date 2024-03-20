from typing import Sequence
from collections import Counter
from cs12232prac05b import first_digits
import math

def first_digits_histogram(data: Sequence[int]) -> list[str]:
    counter: Counter[int] = first_digits(data)

    histogram: list[str] = ['.' * 29] * 20

    cmax: int = max(counter.values())
    index: int = 0

    for i in range(10):
        cd = counter[i]
        height = math.floor(20*cd/cmax)

        for h in range(1, height + 1):
            if index == 0:
                histogram[-h] = "##" + histogram[-h][2:]
            elif index != 0:
                histogram[-h] = histogram[-h][:index] + "##" + histogram[-h][index+2:]
            elif index == 27:
                histogram[-h] = histogram[-h][:index] + "##"
        index += 3

    for row in histogram:
        print(row)

    return histogram