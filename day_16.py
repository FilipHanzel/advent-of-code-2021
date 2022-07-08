from math import prod
from operator import lt, gt, eq
from typing import Tuple, Union


with open("day_16.in", "rt") as f:
    bits = f.read().strip()

# Decode while preserving padding
dec = int("1" + bits, 16)
bits = bin(dec).replace("0b1", "", 1)

cursor = 0


def read(n: int):
    global cursor

    output = bits[cursor : cursor + n]
    cursor += n
    return output


def decode() -> Union[Tuple[int], None]:
    global cursor

    # Parse packet
    version = read(3)
    type_id = read(3)

    version_sum = int(version, 2)  # For part 1
    args = []  # For part 2

    # Parse literal
    if type_id == "100":
        literal = ""
        while True:
            is_next = read(1)
            segment = read(4)
            literal += segment
            if is_next == "0":
                break

        return version_sum, int(literal, 2)

    # Parse operator recursively
    else:
        length_type_id = read(1)

        if length_type_id == "1":
            subpackets = int(read(11), 2)

            for _ in range(subpackets):
                decoded = decode()
                if decoded is not None:
                    version, result = decoded
                    version_sum += version
                    args.append(result)

        else:
            subpackets_bits = int(read(15), 2)

            start = cursor
            while cursor < start + subpackets_bits:
                decoded = decode()
                if decoded is not None:
                    version, result = decoded
                    version_sum += version
                    args.append(result)

    if type_id == "000":
        result = sum(args)
    elif type_id == "001":
        result = prod(args)
    elif type_id == "010":
        result = min(args)
    elif type_id == "011":
        result = max(args)
    elif type_id == "101":
        result = gt(*args)
    elif type_id == "110":
        result = lt(*args)
    elif type_id == "111":
        result = eq(*args)

    return version_sum, int(result)


version_sum, result = decode()
print(f"{version_sum = }")  # Part 1
print(f"{result = }")  # Part 2
