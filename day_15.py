from queue import PriorityQueue
from typing import Tuple, List


def grid_dijkstra(cost_matrix, start: Tuple[int, int], end: Tuple[int, int]):
    def neighbors(x, y, max_rows, max_cols):
        if x > 0:
            yield (x - 1, y)  # Left
        if x < max_rows - 1:
            yield (x + 1, y)  # Right
        if y > 0:
            yield (x, y - 1)  # Up
        if y < max_cols - 1:
            yield (x, y + 1)  # Down

    x, y = start
    rows = len(risk_levels)
    cols = len(risk_levels[0])

    visited = [[False] * cols for row in range(rows)]
    visited[y][x] = True

    # Keep track
    queued = [[False] * cols for row in range(rows)]
    queued[y][x] = True

    distance = [[float("inf")] * cols for row in range(rows)]
    distance[y][x] = 0

    queue = PriorityQueue()

    while True:
        for n_x, n_y in neighbors(x, y, rows, cols):
            if not visited[n_y][n_x]:

                new_cost = distance[y][x] + risk_levels[n_y][n_x]
                if new_cost < distance[n_y][n_x]:
                    distance[n_y][n_x] = new_cost

                if not queued[n_y][n_x]:
                    queue.put((distance[n_y][n_x], (n_x, n_y)))
                    queued[n_y][n_x] = True

        if y == cols - 1 and x == rows - 1:
            break

        visited[y][x] = True
        _, (x, y) = queue.get(block=False)

    return distance[end[1]][end[0]]


with open("day_15.in", "rt") as f:
    risk_levels = [
        [int(risk) for risk in line] for line in f.read().strip().split("\n")
    ]

# Part 1

cost = grid_dijkstra(risk_levels, (0, 0), (-1, -1))
print(f"{cost = }")

# Part 2

# Expand to the right
tile = risk_levels

for _ in range(5 - 1):
    new_tile = [
        [(risk + 1) % 9 if risk + 1 > 9 else risk + 1 for risk in row] for row in tile
    ]

    for row, tile_row in zip(risk_levels, new_tile):
        row.extend(tile_row)

    tile = new_tile

# Expand to the bottom
tiles = risk_levels

for _ in range(5 - 1):
    new_tiles = [
        [(risk + 1) % 9 if risk + 1 > 9 else risk + 1 for risk in row] for row in tiles
    ]

    risk_levels.extend(new_tiles)

    tiles = new_tiles

cost = grid_dijkstra(risk_levels, (0, 0), (-1, -1))
print(f"{cost = }")
