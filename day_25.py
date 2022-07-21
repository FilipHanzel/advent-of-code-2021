with open("day_25.in", "rt") as f:
    seafloor = [list(row) for row in f.read().strip().split("\n")]

height = len(seafloor)
width = len(seafloor[0])

will_move = [[False] * width for _ in range(height)]


def step():
    moves = 0

    # East facing turn

    # Check
    for row in range(height):
        for col in range(width):
            if seafloor[row][col] == ">":
                next_col = (col + 1) % width
                if seafloor[row][next_col] == ".":
                    will_move[row][col] = True
                    moves += 1
            else:
                will_move[row][col] = False

    # Move
    for row in range(height):
        for col in range(width):
            if seafloor[row][col] == ">" and will_move[row][col]:
                next_col = (col + 1) % width
                seafloor[row][col] = "."
                seafloor[row][next_col] = ">"

    # South facing turn

    # Check
    for row in range(height):
        for col in range(width):
            if seafloor[row][col] == "v":
                next_row = (row + 1) % height

                if seafloor[next_row][col] == ".":
                    will_move[row][col] = True
                    moves += 1
            else:
                will_move[row][col] = False

    # Move
    for row in range(height):
        for col in range(width):
            if seafloor[row][col] == "v" and will_move[row][col]:
                next_row = (row + 1) % height
                seafloor[row][col] = "."
                seafloor[next_row][col] = "v"

    return moves


counter = 0
while True:
    moves = step()
    counter += 1

    if moves == 0:
        break

print(f"{counter = }")
