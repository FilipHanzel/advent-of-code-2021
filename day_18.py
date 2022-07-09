from itertools import permutations
from math import floor, ceil


# Add two numbers
def add(a, b):
    number = ["["] + a + b + ["]"]

    while True:
        # Traverse new number looking for explodes
        depth = cursor = 0
        exploded = False
        while cursor < len(number):
            if number[cursor] == "[":
                depth += 1
            elif number[cursor] == "]":
                depth -= 1

            # Explode
            if depth == 4 + 1:
                exploded = True

                # Skip to get to the most nested pair
                while not (
                    isinstance(number[cursor + 1], int)
                    and isinstance(number[cursor + 2], int)
                ):
                    cursor += 1

                # Get the values from the pair
                value_left = number.pop(cursor + 1)
                value_right = number.pop(cursor + 1)

                # Replace parenthesis with 0
                number[cursor : cursor + 2] = [0]

                # Traverse left to find closest number
                for idx in range(cursor - 1, 0, -1):
                    if isinstance(number[idx], int):
                        number[idx] += value_left
                        break

                # Traverse right to find closest number
                for idx in range(cursor + 1, len(number) - 1, 1):
                    if isinstance(number[idx], int):
                        number[idx] += value_right
                        break

                # Start exploding all over again
                depth = cursor = 0
                continue

            cursor += 1

        # Traverse new number looking for splits
        cursor = 0
        splitted = False
        while cursor < len(number):
            if isinstance(number[cursor], int):
                if number[cursor] >= 10:
                    splitted = True

                    value = number.pop(cursor)

                    number[cursor:cursor] = [
                        "[",
                        floor(value / 2),
                        ceil(value / 2),
                        "]",
                    ]

                    # Go back to exploding
                    break

            cursor += 1

        if not exploded and not splitted:
            break

    return number


# Calculate magnitude
def magnitude(number):
    while len(number) > 3:
        cursor = 0

        while cursor < len(number) - 1:
            if (isinstance(number[cursor + 1], int)) and (
                isinstance(number[cursor + 2], int)
            ):
                # Get the values from the pair
                value_left = number.pop(cursor + 1)
                value_right = number.pop(cursor + 1)

                # Calculate and insert
                magnitude = 3 * value_left + 2 * value_right

                # Replace parenthesis with the magnitude
                number[cursor : cursor + 2] = [magnitude]

                cursor += 1
            cursor += 1

    return number[0]


with open("day_18.in", "rt") as f:
    numbers_to_add = f.read().strip().split("\n")
    numbers_to_add = [
        [int(char) if char.isdigit() else char for char in number if char != ","]
        for number in numbers_to_add
    ]

# Part 1

number = numbers_to_add.pop(0)
for next_number in numbers_to_add:
    number = add(number, next_number)

result_magnitude = magnitude(number)

print(f"{result_magnitude = }")

# Part 2


max_pair_magnitude = 0
for pair in permutations(numbers_to_add, 2):
    result = add(*pair)
    mag = magnitude(result)
    max_pair_magnitude = max(max_pair_magnitude, mag)

print(f"{max_pair_magnitude = }")
