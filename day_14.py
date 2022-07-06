from collections import Counter
from functools import lru_cache
from typing import Dict


# Recurrent solution with cache
def count(polymer: str, rules: Dict, starting_depth: int) -> Counter:
    counter = Counter(polymer)

    @lru_cache(maxsize=None)
    def insert(a: str, b: str, depth: int):

        to_insert = rules[a + b]

        counter = Counter(to_insert)

        if depth == 1:
            return counter

        counter += insert(a, to_insert, depth - 1)
        counter += insert(to_insert, b, depth - 1)
        return counter

    # Run recursion for each pair
    for idx in range(len(polymer) - 1):
        counter += insert(polymer[idx], polymer[idx + 1], starting_depth)

    return counter


with open("day_14.in", "rt") as f:
    template, rules = f.read().split("\n\n")

rules = dict(rule.split(" -> ") for rule in rules.split("\n"))

# Part 1

most_common, *_, least_common = count(template, rules, starting_depth=10).most_common()
most_common, least_common = most_common[1], least_common[1]
print(f"{most_common - least_common = }")

# Part 2

most_common, *_, least_common = count(template, rules, starting_depth=40).most_common()
most_common, least_common = most_common[1], least_common[1]
print(f"{most_common - least_common = }")
