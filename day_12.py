from typing import List

with open("day_12.in", "rt") as f:
    puzzle_input = [line.split("-") for line in f.read().strip().split("\n")]


# Build a dicitionary with all possible paths from each point
directions = {}
for a, b in puzzle_input:

    if b == "start" or a == "end":
        a, b = b, a

    if a not in directions:
        directions[a] = []
    directions[a].append(b)

    if a != "start" and b != "end":
        if b not in directions:
            directions[b] = []
        directions[b].append(a)


# Part 1


def step(position: str = "start", small_passed: List[str] = []):
    paths = 0
    for next_position in directions[position]:

        # Close the path if reached the end
        if next_position == "end":
            paths += 1

        elif next_position.islower():
            # Dead end - already passed small cave and next is small
            if next_position in small_passed:
                continue

            small_passed.append(next_position)
            paths += step(next_position, small_passed)
            small_passed.pop()

        else:
            paths += step(next_position, small_passed)

    return paths


paths = step()

print(f"{paths = }")

# Part 2


def step(
    position: str = "start",
    small_passed: List[str] = [],
    second_pass_used: bool = False,
):
    paths = 0
    for next_position in directions[position]:

        # Close the path if reached the end
        if next_position == "end":
            paths += 1

        elif next_position.islower():
            # Check if already visited next_position
            using_second_pass = next_position in small_passed

            # Dead end - we need to use second pass, but it was used already
            if using_second_pass and second_pass_used:
                continue

            small_passed.append(next_position)
            paths += step(
                next_position,
                small_passed,
                # In the next step there might be small cave passed twice
                second_pass_used or using_second_pass,
            )
            small_passed.pop()
        else:
            paths += step(next_position, small_passed, second_pass_used)

    return paths


paths = step()

print(f"{paths = }")
