with open("day_04.in", "rt") as f:
    draw_order = [int(value) for value in f.readline().split(",")]
    boards = [
        [[int(value) for value in row.split()] for row in board.split("\n")]
        for board in f.read().strip().split("\n\n")
    ]


def scores_generator(draw_order, boards):
    winning_boards = [False] * len(boards)
    flagged_numbers = [[[False] * len(row) for row in board] for board in boards]

    def is_winning(board_index):
        for row in flagged_numbers[board_index]:
            if sum(row) == len(row):
                return True

        for column in zip(*flagged_numbers[board_index]):
            if sum(column) == len(column):
                return True

        return False

    def mark(board_index, number):
        rows = len(boards[0])
        cols = len(boards[0][0])

        for row_index in range(rows):
            for column_index in range(cols):
                if boards[board_index][row_index][column_index] == number:
                    flagged_numbers[board_index][row_index][column_index] = True

    def calculate_score(winning_board, flagged, last_number):
        unmarked_sum = 0

        rows = len(boards[0])
        cols = len(boards[0][0])
        for row_index in range(rows):
            for column_index in range(cols):
                if not flagged[row_index][column_index]:
                    unmarked_sum += winning_board[row_index][column_index]

        return unmarked_sum * last_number

    for number in draw_order:
        for board_index in range(len(boards)):
            if winning_boards[board_index]:
                continue

            mark(board_index, number)
            if is_winning(board_index):
                yield calculate_score(
                    winning_board=boards[board_index],
                    flagged=flagged_numbers[board_index],
                    last_number=number,
                )
                winning_boards[board_index] = True


scores = scores_generator(draw_order, boards)
score = next(scores)

print(f"{score = }")

for score in scores:
    pass

print(f"{score = }")
