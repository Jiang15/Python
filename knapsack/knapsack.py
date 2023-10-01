""" A recursive implementation of 0-N Knapsack Problem
    https://en.wikipedia.org/wiki/Knapsack_problem
"""
from __future__ import annotations
from functools import lru_cache


def knapsack(
    capacity: int,
    weights: list[int],
    values: list[int],
    counter: int,
    allow_repetition=False,
) -> int:
    """
    Returns the maximum value that can be put in a knapsack of a capacity cap,
    whereby each weight w has a specific value val with option to allow repetitive selection of items

    >>> cap = 50
    >>> val = [60, 100, 120]
    >>> w = [10, 20, 30]
    >>> c = len(val)
    >>> knapsack(cap, w, val, c, False)
    220

    Given the repetition is NOT allowed,
    the result is 220 cause the values of 100 and 120 got the weight of 50
    which is the limit of the capacity.
    >>> knapsack(cap, w, val, c, True)
    300

    Given the repetition is allowed,
    tthe result is 300 cause the values of 60*5 (pick 5 times)
    which is the limit of the capacity.
    """

    @lru_cache()
    def knapsack_recur(cap: int, c: int) -> int:
        # Base Case
        if c == 0 or cap == 0:
            return 0

        # If weight of the nth item is more than Knapsack of capacity,
        #   then this item cannot be included in the optimal solution,
        # else return the maximum of two cases:
        #   (1) not included
        #   (2) nth item included one or more times (0-N), if allow_repetition is true
        #       nth item included only once (0-1), if allow_repetition is false
        if weights[c - 1] > cap:
            return knapsack_recur(cap, c - 1)
        else:
            without_new_value = knapsack_recur(cap, c - 1)
            if allow_repetition:
                new_value_included = values[c - 1] + knapsack_recur(
                    cap - weights[c - 1], c
                )
            else:
                new_value_included = values[c - 1] + knapsack_recur(
                    cap - weights[c - 1], c - 1
                )
            return max(new_value_included, without_new_value)

    return knapsack_recur(capacity, counter)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
