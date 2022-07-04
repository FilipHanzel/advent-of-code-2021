with open("day_07.in", "rt") as f:
    puzzle_input = [int(position) for position in f.read().strip().split(",")]

# Part 1

min_fuel_consumed = None

for position in range(0, max(puzzle_input) + 1):
    fuel_consumed = 0
    for crab_position in puzzle_input:
        fuel_consumed += abs(crab_position - position)

    min_fuel_consumed = (
        fuel_consumed
        if min_fuel_consumed is None
        else min(min_fuel_consumed, fuel_consumed)
    )

print(f"{min_fuel_consumed = }")

# Part 2

min_fuel_consumed = None

for position in range(0, max(puzzle_input) + 1):
    fuel_consumed = 0
    for crab_position in puzzle_input:
        distance = abs(crab_position - position)
        fuel_consumed += distance * (distance + 1) // 2

    min_fuel_consumed = (
        fuel_consumed
        if min_fuel_consumed is None
        else min(min_fuel_consumed, fuel_consumed)
    )

print(f"{min_fuel_consumed = }")
