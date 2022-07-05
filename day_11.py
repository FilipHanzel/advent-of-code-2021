with open("day_11.in", "rt") as f:
    energy_levels = [list(map(int, line)) for line in f.read().strip().split("\n")]

grid_size = 10


def flash(y: int, x: int):
    # Recursive flash

    energy_levels[y][x] = -1

    flashes = 1

    # Adjusted window to avoid index error
    y_start = max(y - 1, 0)
    x_start = max(x - 1, 0)
    y_end = min(y + 2, grid_size)
    x_end = min(x + 2, grid_size)

    for yy in range(y_start, y_end):
        for xx in range(x_start, x_end):

            # Skip octopus if it flashed in this step
            if energy_levels[yy][xx] == -1:
                continue

            # Increase energy levels of adjacent octopus
            if (y != yy) or (x != xx):
                energy_levels[yy][xx] += 1

                # Flash adjacent octopus
                if energy_levels[yy][xx] > 9:
                    flashes += flash(yy, xx)

    return flashes


flashes_after_100_steps = 0  # For part 1

step = 0
completed = False
while not completed:

    flashes_at_any_step = 0  # For part 2

    # Increase energy levels
    for y in range(grid_size):
        for x in range(grid_size):
            energy_levels[y][x] += 1

    # Chain flash
    for y in range(grid_size):
        for x in range(grid_size):
            if energy_levels[y][x] > 9:
                flashes = flash(y, x)

                # For part 1
                if step < 100:
                    flashes_after_100_steps += flashes

                # For part 2
                flashes_at_any_step += flashes

    # Reset flashed to 0
    for y in range(grid_size):
        for x in range(grid_size):
            if energy_levels[y][x] == -1:
                energy_levels[y][x] = 0

    step += 1

    # End when both parts 1 and 2 are completed
    if step > 100 and flashes_at_any_step == 100:
        completed = True


print(f"{flashes_after_100_steps = }")
print(f"{step = }")
