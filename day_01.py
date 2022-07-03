with open("day_01.in", "rt") as f:
    puzzle_input = [int(line) for line in f.read().strip().split()]

# Part 1

increases = 0
last = None
for measurement in puzzle_input:
    if last is not None and measurement > last:
        increases += 1
    last = measurement

print(f"{increases = }")

# Part 2

windowed = []
windows_count = len(puzzle_input) - 2
for i in range(windows_count):
    window = puzzle_input[i] + puzzle_input[i + 1] + puzzle_input[i + 2]
    windowed.append(window)

increases = 0
last = None
for measurement in windowed:
    if last is not None and measurement > last:
        increases += 1
    last = measurement

print(f"{increases = }")
