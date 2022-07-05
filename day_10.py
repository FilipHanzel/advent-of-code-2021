with open("day_10.in", "rt") as f:
    puzzle_input = f.read().strip().split("\n")

# Part 1


def is_paired(opening: str, closing: str):
    if opening == "(":
        return closing == ")"
    if opening == "[":
        return closing == "]"
    if opening == "{":
        return closing == "}"
    if opening == "<":
        return closing == ">"
    raise ValueError(f'No matching character found for "{opening}"')


def get_syntax_score(character: str):
    if character == ")":
        return 3
    if character == "]":
        return 57
    if character == "}":
        return 1197
    if character == ">":
        return 25137


syntax_score = 0
incomplete_stacks = []  # For part 2

for line in puzzle_input:
    stack = []
    for char in line:
        # If the character is opening - add it to the stack
        if char in "([{<":
            stack.append(char)
        # If the character is closing - check if it matches
        else:
            last = stack.pop()
            if not is_paired(last, char):
                syntax_score += get_syntax_score(char)
                break
    else:
        incomplete_stacks.append(stack)  # For part 2

print(f"{syntax_score = }")

# Part 2


def get_autocomplete_score_mirror(character: str):
    if character == "(":
        return 1
    if character == "[":
        return 2
    if character == "{":
        return 3
    if character == "<":
        return 4


scores = []
for stack in incomplete_stacks:
    score = 0
    for char in reversed(stack):
        score *= 5
        score += get_autocomplete_score_mirror(char)
    scores.append(score)

scores = sorted(scores)
middle_autocomplete_score = scores[len(scores) // 2]

print(f"{middle_autocomplete_score = }")
