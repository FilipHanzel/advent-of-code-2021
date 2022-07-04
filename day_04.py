with open("day_04.in", "rt") as f:
    draw_order = [int(value) for value in f.readline().split(",")]
    boards = [
        [[int(value) for value in row.split()] for row in board.split("\n")]
        for board in f.read().strip().split("\n\n")
    ]


board_count = len(boards)
grid_size = len(boards[0])

# Keep track of winning boards
is_winning = [False] * board_count
# Keep track of drawn numbers
drawn = [[[False] * grid_size for row in board] for board in boards]


first_winning_score = None
last_winning_score = None

for number in draw_order:

    if all(is_winning):
        break

    for board_index in range(board_count):
        # Do not check a board that is already winning
        if is_winning[board_index]:
            continue

        # Set a flag that number was already chosen
        for row_index in range(grid_size):
            for col_index in range(grid_size):
                if boards[board_index][row_index][col_index] == number:
                    drawn[board_index][row_index][col_index] = True

        # Search for full row or column
        won = False
        for row in drawn[board_index]:
            if sum(row) == grid_size:
                won = True
                break
        else:
            for column in zip(*drawn[board_index]):
                if sum(column) == grid_size:
                    won = True
                    break

        if won:
            # Mark board as winning
            is_winning[board_index] = True

            # Calculate score for the board
            unmarked_sum = 0
            for row_index in range(grid_size):
                for col_index in range(grid_size):
                    if not drawn[board_index][row_index][col_index]:
                        unmarked_sum += boards[board_index][row_index][col_index]

            score = unmarked_sum * number

            # Save scores
            if first_winning_score is None:
                first_winning_score = score
            last_winning_score = score


print(f"{first_winning_score = }")
print(f"{last_winning_score = }")
