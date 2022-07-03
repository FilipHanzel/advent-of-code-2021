with open("day_02.in", "rt") as f:
    puzzle_input = []
    for line in f.read().strip().split("\n"):
        direction, value = line.split()
        puzzle_input.append((direction, int(value)))

# Part 1

horizontal = 0
depth = 0

for direction, distance in puzzle_input:
    if direction == "forward":
        horizontal += distance

    elif direction == "down":
        depth += distance

    elif direction == "up":
        depth -= distance

print(f"{horizontal * depth = }")

# Part 2

horizontal = 0
depth = 0
aim = 0

for direction, value in puzzle_input:
    if direction == "forward":
        horizontal += value
        depth += aim * value

    elif direction == "down":
        aim += value

    elif direction == "up":
        aim -= value

print(f"{horizontal * depth = }")
