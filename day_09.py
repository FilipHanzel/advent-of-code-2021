with open("day_09.in", "rt") as f:
    heightmap = [list(map(int, line)) for line in f.read().strip().split("\n")]

rows = len(heightmap)
cols = len(heightmap[0])

low_points = []

# Get low points
for y in range(rows):
    for x in range(cols):

        # Check up
        if y > 0:
            if heightmap[y][x] >= heightmap[y - 1][x]:
                continue
        # Check down
        if y < rows - 1:
            if heightmap[y][x] >= heightmap[y + 1][x]:
                continue
        # Check left
        if x > 0:
            if heightmap[y][x] >= heightmap[y][x - 1]:
                continue
        # Check right
        if x < cols - 1:
            if heightmap[y][x] >= heightmap[y][x + 1]:
                continue

        # Found low point
        low_points.append((y, x))

# Part 1

risk_levels_sum = 0
for y, x in low_points:
    risk_levels_sum += 1 + heightmap[y][x]

print(f"{risk_levels_sum = }")

# Part 2

visited = [[False] * cols for row in range(rows)]


def check_point(y: int, x: int):
    # Check points recursively
    size = 1
    visited[y][x] = True

    # Check up
    if y > 0:
        if heightmap[y - 1][x] != 9 and not visited[y - 1][x]:
            size += check_point(y - 1, x)

    # Check down
    if y < rows - 1:
        if heightmap[y + 1][x] != 9 and not visited[y + 1][x]:
            size += check_point(y + 1, x)

    # Check left
    if x > 0:
        if heightmap[y][x - 1] != 9 and not visited[y][x - 1]:
            size += check_point(y, x - 1)

    # Check right
    if x < cols - 1:
        if heightmap[y][x + 1] != 9 and not visited[y][x + 1]:
            size += check_point(y, x + 1)

    return size


basin_sizes = [check_point(y, x) for y, x in low_points]

largest_basins_mul = 1
for size in sorted(basin_sizes, reverse=True)[:3]:
    largest_basins_mul *= size

print(f"{largest_basins_mul = }")
