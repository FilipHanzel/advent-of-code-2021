from itertools import combinations
from pprint import pprint

with open("day_19.in", "rt") as f:
    scanners = []
    for scanner in f.read().strip().split("\n\n"):
        _, *readings = scanner.split("\n")
        readings = {tuple(map(int, reading.split(","))) for reading in readings}
        scanners.append(readings)

required_overlap = 12

# Calculate potential matches using common distances between points


def square_euclidean(list_a, list_b):
    distance = 0
    for x_coord, y_coord in zip(list_a, list_b):
        distance += (x_coord - y_coord) ** 2
    return distance


distances = []

for scanner in scanners:
    scanner_distances = [square_euclidean(x, y) for x, y in combinations(scanner, 2)]
    distances.append(scanner_distances)

min_common_dist = required_overlap * (required_overlap - 1) // 2

potential_matches = []

for i in range(len(scanners) - 1):
    for j in range(i, len(scanners)):
        if i == j:
            continue

        a_dist = set(distances[i])
        b_dist = set(distances[j])
        common_dist = a_dist.intersection(b_dist)

        if len(common_dist) >= min_common_dist:
            potential_matches.append((i, j))
            potential_matches.append((j, i))


def rotations():
    for orientation in (
        (0, 1, 2),
        (2, 0, 1),
        (1, 2, 0),
    ):
        x, y, z = orientation

        # 4 rotations
        yield lambda p: (p[x], p[y], p[z])
        yield lambda p: (p[z], p[y], -p[x])
        yield lambda p: (-p[x], p[y], -p[z])
        yield lambda p: (-p[z], p[y], p[x])

        # mirror and 4 other rotations
        yield lambda p: (-p[x], -p[y], p[z])
        yield lambda p: (p[z], -p[y], p[x])
        yield lambda p: (p[x], -p[y], -p[z])
        yield lambda p: (-p[z], -p[y], -p[x])


# Check all possible rotations and translations to fing matches


def find_match(scanner_a, scanner_b):
    for to_point in scanner_a:
        for rotation in rotations():
            rotated_b = {rotation(point) for point in scanner_b}

            for from_point in rotated_b:

                translation = tuple(f - t for f, t in zip(from_point, to_point))
                translated_b = {
                    tuple(p - c for p, c in zip(point, translation))
                    for point in rotated_b
                }

                common_points = scanner_a.intersection(translated_b)

                if len(common_points) >= required_overlap:
                    scanner_position = tuple(-p for p in translation)  # For part 2
                    return translated_b, scanner_position


# Translate and rotate found matches to the coordinate system of scanner 0
# (translated_to_0 will fill up while iterating on it)

positions = [None] * len(scanners)
positions[0] = (0, 0, 0)

moved_to_0 = [0]
for i in moved_to_0:
    a = scanners[i]

    # Check only scanners that were not already matched
    left_to_check = set(range(len(scanners))).difference(moved_to_0)

    for j in left_to_check:
        if (i, j) not in potential_matches:
            continue

        b = scanners[j]

        result = find_match(a, b)

        if result is not None:
            moved_scanner, scanner_position = result

            scanners[j] = moved_scanner
            positions[j] = scanner_position

            moved_to_0.append(j)


# Collapse all readings into one set to get number of beacons

common = set()
for scanner in scanners:
    common.update(scanner)

beacons = len(common)
print(f"{beacons = }")

# Calculate manhattan distance


def manhattan(a, b):
    distance = 0
    for dim_a, dim_b in zip(a, b):
        distance += abs(dim_a - dim_b)
    return distance


max_distance = 0
for position_a, position_b in combinations(positions, 2):
    max_distance = max(max_distance, manhattan(position_a, position_b))

print(f"{max_distance = }")
