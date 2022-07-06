with open("day_13.in", "rt") as f:
    raw_coords, raw_folds = f.read().strip().split("\n\n")

coords = []
for coord in raw_coords.split("\n"):
    x, y = coord.split(",")
    x = int(x)
    y = int(y)
    coords.append([x, y])

folds = []
for fold in raw_folds.split("\n"):
    axis, value = fold.split()[-1].split("=")
    folds.append((axis, int(value)))


# Change each point accordingly without making a matrix
for i, (axis, value) in enumerate(folds):
    axis = 0 if axis == "x" else 1

    for point in coords:
        if point[axis] > value:
            point[axis] = 2 * value - point[axis]

    # Part 1

    if i == 0:
        # Deduplicate coords
        unique = []
        for point in coords:
            if point not in unique:
                unique.append(point)

        visible_dots = len(unique)
        print(f"{visible_dots = }")

        # Might as well use deduplicated coords from now on
        coords = unique

# Part 2 (print the result)

max_x = 0
max_y = 0
for x, y in coords:
    max_x = max(max_x, x + 1)
    max_y = max(max_y, y + 1)

dots = [[False] * max_x for row in range(max_y)]

for x, y in coords:
    dots[y][x] = True

for row in dots:
    print("".join([" " if not e else "█" for e in row]))
