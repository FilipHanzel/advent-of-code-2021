from typing import List, Tuple

with open("day_22.in", "rt") as f:
    steps = []
    for step in f.read().strip().split("\n"):
        action, ranges = step.split()

        x_range, y_range, z_range = ranges.split(",")
        x_range = tuple(map(int, x_range.lstrip("x=").split("..")))
        y_range = tuple(map(int, y_range.lstrip("y=").split("..")))
        z_range = tuple(map(int, z_range.lstrip("z=").split("..")))

        step = (action, x_range, y_range, z_range)
        steps.append(step)

#  Part 1 (naive solution)

# Initialization cube axis order: init_cube[y][x][z]
init_cube_size = 100 + 1
init_cube = [
    [[0] * init_cube_size for _ in range(init_cube_size)] for _ in range(init_cube_size)
]

for action, x_range, y_range, z_range in steps:
    # Cap cuboids at ranges within initialization cube
    # and shift coordinates from [-50:50] to [0:100] range

    x_min, x_max = x_range
    x_min = max(-50, x_min) + 50
    x_max = min(50, x_max) + 50

    y_min, y_max = y_range
    y_min = max(-50, y_min) + 50
    y_max = min(50, y_max) + 50

    z_min, z_max = z_range
    z_min = max(-50, z_min) + 50
    z_max = min(50, z_max) + 50

    # Switch qubes

    action = 1 if action == "on" else 0

    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            for z in range(z_min, z_max + 1):
                init_cube[y][x][z] = action

cubes_on = 0
for row in init_cube:
    for col in row:
        cubes_on += sum(col)

print(f"{cubes_on = }")


# Part 2 (suboptimal, but easy to implement)


def get_overlap(ranges_a: Tuple, ranges_b: Tuple) -> List:
    overlap = []
    for range_a, range_b in zip(ranges_a, ranges_b):
        if range_a[0] > range_b[1]:
            return
        if range_a[1] < range_b[0]:
            return

        range_overlap_min = max(range_a[0], range_b[0])
        range_overlap_max = min(range_a[1], range_b[1])
        overlap.append((range_overlap_min, range_overlap_max))

    return overlap


def get_volume(ranges):
    volume = 1
    for start, end in ranges:
        volume *= end - start + 1
    return volume


cube_stack = []
steps = iter(steps)

# If there are any "off" steps at the beggining - ignore
# and add first "on" step to the stack
for step in steps:
    if step[0] == "on":
        cube_stack.append(step)
        break

for action, *ranges in steps:
    step_stack = []

    # For all "on" actions - add that cuboid to the stack
    if action == "on":
        step_stack.append(("on", *ranges))

    # For each cube from the stack calculate overlap
    for stack_action, *stack_ranges in cube_stack:
        overlap = get_overlap(ranges, stack_ranges)
        if overlap is None:
            continue

        # Add the overlapping part with "off"
        if action == "on" and stack_action == "on":
            step_stack.append(("off", *overlap))
        # Add overlapping part with "on" - since "off" steps on the stack are only
        # overlaps with other "on" steps on the stack and for those "on" steps
        # we add "off" overlaps in this step - we need to make up for it here
        elif action == "on" and stack_action == "off":
            step_stack.append(("on", *overlap))
        # Add overlapping part with "off"
        elif action == "off" and stack_action == "on":
            step_stack.append(("off", *overlap))
        # Add overlapping part with "on" - similar reasoning as in second condition
        elif action == "off" and stack_action == "off":
            step_stack.append(("on", *overlap))

    cube_stack.extend(step_stack)

# Add volumes that are "on" and subtract those that are "off" to get number of cubes "on"
cubes_on = 0
for action, *ranges in cube_stack:
    if action == "on":
        cubes_on += get_volume(ranges)
    elif action == "off":
        cubes_on -= get_volume(ranges)

print(f"{cubes_on = }")
