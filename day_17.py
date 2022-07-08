with open("day_17.in", "rt") as f:
    *_, x, y = f.read().strip().split()

    x_min, x_max = tuple(map(int, x.strip("x=,").split("..")))
    y_min, y_max = tuple(map(int, y.strip("y=,").split("..")))


def check_hit(x_vel: int, y_vel: int):
    global x_min, x_max
    global y_min, y_max

    x = y = 0

    while True:
        x += x_vel
        y += y_vel

        x_vel = max(0, x_vel - 1)
        y_vel -= 1

        if (x_min <= x <= x_max) and (y_min <= y <= y_max):
            return True

        if (x > x_max) or (y < y_min):
            return False


def get_height(y_vel):
    return y_vel * (y_vel + 1) // 2


highest_position = None  # For part 1
valid_velocities = 0  # For part 2

# Assuming y_max < 0 and x_min > 0

min_y_vel = y_min - 1
max_y_vel = -y_min + 1
min_x_vel = 0
max_x_vel = x_max + 1


for y_vel in reversed(range(min_y_vel, max_y_vel)):
    for x_vel in range(min_x_vel, max_x_vel):
        if check_hit(x_vel, y_vel):

            if highest_position is None:
                highest_position = get_height(y_vel)

            valid_velocities += 1

print(f"{highest_position = }")
print(f"{valid_velocities = }")
