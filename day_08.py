with open("day_08.in", "rt") as f:
    puzzle_input = []
    for line in f.read().strip().split("\n"):
        patterns, outputs = line.split(" | ")

        patterns = patterns.split()
        outputs = outputs.split()

        puzzle_input.append((patterns, outputs))

# Part 1

easy_digits = 0
for _, outputs in puzzle_input:
    for length in map(len, outputs):
        if length in (2, 4, 3, 7):
            easy_digits += 1

print(f"{easy_digits = }")

# Part 2

outputs_sum = 0

for patterns, outputs in puzzle_input:
    patterns = [set(p) for p in patterns]
    # Each index represents a digit and value on the list - pattern
    digits = [None] * 10

    # Match scrumbled patterns to digits

    # Get patterns for 1, 4, 7 and 8
    for pattern in patterns:
        length = len(pattern)

        if length == 2:
            digits[1] = pattern
        elif length == 4:
            digits[4] = pattern
        elif length == 3:
            digits[7] = pattern
        elif length == 7:
            digits[8] = pattern

    of_length_5 = [p for p in patterns if len(p) == 5]  # patterns for 2, 3 and 5
    of_length_6 = [p for p in patterns if len(p) == 6]  # patterns for 0, 6 and 9

    for pattern in of_length_6:
        # 1 and 6 have one common segment
        # (1 and 0 or 1 and 9 have two common segments)
        common = digits[1].intersection(pattern)
        if len(common) == 1:
            digits[6] = pattern
        else:
            # 4 and 0 have three common segments
            # (4 and 9 have four common segments)
            common = digits[4].intersection(pattern)
            if len(common) == 3:
                digits[0] = pattern
            else:
                # Not 6 and not 0
                digits[9] = pattern

    for pattern in of_length_5:
        # 1 and 3 have two common segments
        # (1 and 2 or 1 and 5 have one common segment)
        common = digits[1].intersection(pattern)
        if len(common) == 2:
            digits[3] = pattern
        else:
            # 4 and 2 have two common segments
            # (4 and 3 or 4 and 5 have 3 common segments)
            common = digits[4].intersection(pattern)
            if len(common) == 2:
                digits[2] = pattern
            else:
                # Not 3 and not 2
                digits[5] = pattern

    # Decode output values

    outputs = [set(o) for o in outputs]

    number = ""
    for output in outputs:
        number += str(digits.index(output))

    outputs_sum += int(number)

print(f"{outputs_sum = }")
