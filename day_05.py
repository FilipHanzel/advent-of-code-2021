with open("day_05.in", "rt") as f:
    max_x = 0
    max_y = 0

    lines = []
    for line in f.read().strip().split("\n"):
        point_1, point_2 = line.split(" -> ")

        x1, y1 = map(int, point_1.split(","))
        x2, y2 = map(int, point_2.split(","))

        lines.append(((x1, y1), (x2, y2)))

        max_x = max(max_x, x1, x2)
        max_y = max(max_y, y1, y2)

# Keep track of how many times each point was on a line
counts = [[0] * (max_x + 1) for _ in range(max_y + 1)]

# Part 1 (horizontal and vertical)

for (x1, y1), (x2, y2) in lines:

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            counts[y][x1] += 1

    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            counts[y1][x] += 1

overlaps = 0
for row in counts:
    for count in row:
        overlaps += count >= 2

print(f"{overlaps = }")

# Part 2 (diagonals)


for (x1, y1), (x2, y2) in lines:

    # Bottom right to top left
    if x1 > x2 and y1 > y2:
        for i in range(x1 - x2 + 1):
            counts[y2 + i][x2 + i] += 1

    # Top left to bottom right
    elif x1 < x2 and y1 < y2:
        for i in range(x2 - x1 + 1):
            counts[y1 + i][x1 + i] += 1

    # Bottom left to top right
    elif x1 > x2 and y1 < y2:
        for i in range(x1 - x2 + 1):
            counts[y1 + i][x1 - i] += 1

    # Top right to bottom left
    elif x1 < x2 and y1 > y2:
        for i in range(x2 - x1 + 1):
            counts[y1 - i][x1 + i] += 1

overlaps = 0
for row in counts:
    for count in row:
        overlaps += count >= 2

print(f"{overlaps = }")
