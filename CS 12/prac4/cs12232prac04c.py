from typing import Sequence, TypeVar

I = TypeVar("I", bound = int | str | tuple[int, int])
P = TypeVar("P")

def sort_parcels(orders: Sequence[tuple[I, P]]) -> dict[I, list[P]]:
    sorted_orders: dict[I, list[P]] = {}

    for order in orders:
        if order[0] in sorted_orders:
            sorted_orders[order[0]].append(order[1])
        else:
            sorted_orders[order[0]] = [order[1]]

    return dict(sorted(sorted_orders.items()))