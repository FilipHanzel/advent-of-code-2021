class SquidBingo:
    def __init__(self, boards, draw_order):
        self.boards = boards
        self.draw_order = draw_order

        self.rows = len(boards[0])
        self.cols = len(boards[0][0])
        self.is_winning = [False] * len(boards)
        self.flagged = [[[False] * len(row) for row in board] for board in boards]

    def _check_if_wins(self, board_index):
        for row in self.flagged[board_index]:
            if sum(row) == self.rows:
                return True

        for column in zip(*self.flagged[board_index]):
            if sum(column) == self.cols:
                return True

        return False

    def _flag(self, board_index, number):
        for row_index in range(self.rows):
            for col_index in range(self.cols):
                if self.boards[board_index][row_index][col_index] == number:
                    self.flagged[board_index][row_index][col_index] = True

    def _calculate_score(self, board_index, last_number):
        unmarked_sum = 0

        for row_index in range(self.rows):
            for col_index in range(self.cols):
                if not self.flagged[board_index][row_index][col_index]:
                    unmarked_sum += self.boards[board_index][row_index][col_index]

        return unmarked_sum * last_number

    def solve(self):
        first_score = None
        last_score = None

        for number in self.draw_order:

            if all(self.is_winning):
                break

            for board_index in range(len(self.boards)):

                if self.is_winning[board_index]:
                    continue

                self._flag(board_index, number)

                if self._check_if_wins(board_index):
                    score = self._calculate_score(board_index, number)
                    if first_score is None:
                        first_score = score
                    last_score = score

                    self.is_winning[board_index] = True

        return first_score, last_score


with open("day_04.in", "rt") as f:
    draw_order = [int(value) for value in f.readline().split(",")]
    boards = [
        [[int(value) for value in row.split()] for row in board.split("\n")]
        for board in f.read().strip().split("\n\n")
    ]

bingo = SquidBingo(boards, draw_order)
first_winning_score, last_winning_score = bingo.solve()
print(f"{first_winning_score = }")
print(f"{last_winning_score = }")
