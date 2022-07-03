with open("day_03.in", "rt") as f:
    puzzle_input = f.read().strip().split()

# Part 1

gamma = ""
epsilon = ""

for column in zip(*puzzle_input):
    ones = column.count("1")
    zeros = len(column) - ones

    if ones > zeros:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(f"{gamma * epsilon = }")

# Part 2


def get_counts(report, column_index):
    ones = 0
    for row in report:
        ones += row[column_index] == "1"

    return ones, len(report) - ones


def drop_records(report, column_index, number):
    # Iterate over reversed report indexes
    for record_index in range(len(report) - 1, -1, -1):
        if number == report[record_index][column_index]:
            del report[record_index]


columns_count = len(puzzle_input[0])

generator = puzzle_input.copy()
for column_index in range(columns_count):
    ones, zeros = get_counts(generator, column_index)
    drop_records(generator, column_index, "1" if ones >= zeros else "0")

    if len(generator) == 1:
        break

scrubber = puzzle_input.copy()
for column_index in range(columns_count):
    ones, zeros = get_counts(scrubber, column_index)
    drop_records(scrubber, column_index, "0" if ones >= zeros else "1")

    if len(scrubber) == 1:
        break

generator = int(generator[0], 2)
scrubber = int(scrubber[0], 2)

print(f"{generator * scrubber = }")
