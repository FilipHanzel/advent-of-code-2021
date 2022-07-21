with open("day_24.in", "rt") as f:
    instr = [line.split() for line in f.read().strip().split("\n")]

# There are 14 repeating blocks of instructions each starting with inp.
# Variable z can be treated as a stack of numbers with base 26. Each time
# 5th instruction is "div z 1", we append a number to this stack. We pop from
# the stack if 5th instruction is "div z 26" and paired together with block
# "div z 1" (from the top of the stack) meet the condition:
#
#   inp_for_div26 == inp_for_div1 + y + x
#
# where y is the value from 16th instruction from block with "div z 1" and x is
# 6th instruction from block with "div z 26". Stack has to be empty when MONAD
# finishes in order for variable z to be 0. Since there are 7 instructions that
# append to the stack (div z 1) and 7 instructions that can pop from the stack
# (div z 26), the condition has to be met for each "pair" of instructions
# (pop from stack as often as possible).

blocks = 14
block_size = len(instr) // blocks

temp_stack, pairs = [], []

for block_idx in range(blocks):
    offset = block_idx * block_size

    block_type = instr[offset + 4][-1]

    if block_type == "1":
        div = {"add_y": int(instr[offset + 15][-1]), "idx": block_idx}
        temp_stack.append(div)
    else:
        div = {"add_x": int(instr[offset + 5][-1]), "idx": block_idx}
        pairs.append({"div_1": temp_stack.pop(), "div_26": div})


def solve_pair_for_max(y: int, x: int):
    for inp_26 in range(9, 0, -1):
        for inp_1 in range(9, 0, -1):
            if inp_26 == inp_1 + y + x:
                return inp_26, inp_1


def solve_pair_for_min(y: int, x: int):
    for inp_26 in range(1, 9 + 1):
        for inp_1 in range(1, 9 + 1):
            if inp_26 == inp_1 + y + x:
                return inp_26, inp_1


model_num_max = [None] * 14  # For part 1
model_num_min = [None] * 14  # For part 2

for pair in pairs:

    div_1_y = pair["div_1"]["add_y"]
    div_26_x = pair["div_26"]["add_x"]

    div_1_idx = pair["div_1"]["idx"]
    div_26_idx = pair["div_26"]["idx"]

    # Part 1

    inp_26, inp_1 = solve_pair_for_max(div_1_y, div_26_x)

    model_num_max[div_1_idx] = inp_1
    model_num_max[div_26_idx] = inp_26

    # Part 2

    inp_26, inp_1 = solve_pair_for_min(div_1_y, div_26_x)

    model_num_min[div_1_idx] = inp_1
    model_num_min[div_26_idx] = inp_26

model_num_max = "".join(map(str, model_num_max))
model_num_min = "".join(map(str, model_num_min))
print(f"{model_num_max = }")
print(f"{model_num_min = }")
