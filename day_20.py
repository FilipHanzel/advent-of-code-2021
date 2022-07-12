from copy import deepcopy
from typing import List


with open("day_20.in", "rt") as f:
    algorithm, input_image = f.read().strip().split("\n\n")

    input_image = [list(line) for line in input_image.split("\n")]


def translate(number: List) -> int:
    idx = ""
    for char in number:
        idx += "1" if char == "#" else "0"
    return int(idx, 2)


def pad(image, char=".") -> None:
    image = deepcopy(image)

    width = len(image[0])

    image[0:0] = [[char] * width, [char] * width]
    image += [[char] * width, [char] * width]

    for row in image:
        row[0:0] = [char] * 2
        row += [char] * 2

    return image


def enhance(image):
    width = len(image[0])
    height = len(image)

    new_image = []
    for row in range(height - 2):
        min_row = row
        max_row = row + 3

        new_row = []

        for col in range(width - 2):
            min_col = col
            max_col = col + 3

            number = []

            for window_row in range(min_row, max_row):
                number += image[window_row][min_col:max_col]

            number = translate(number)
            new_row.append(algorithm[number])

        new_image.append(new_row)

    return new_image


# Part 1


reprtitions = 2
padding_char = "."

image = input_image
for _ in range(reprtitions):
    image = pad(image, padding_char)
    image = enhance(image)
    padding_char = algorithm[0 if padding_char == "." else -1]

lit_pixels = 0
for row in image:
    lit_pixels += row.count("#")

print(f"{lit_pixels = }")


# Part 2


reprtitions = 50
padding_char = "."

image = input_image
for _ in range(reprtitions):
    image = pad(image, padding_char)
    image = enhance(image)
    padding_char = algorithm[0 if padding_char == "." else -1]

lit_pixels = 0
for row in image:
    lit_pixels += row.count("#")

print(f"{lit_pixels = }")
