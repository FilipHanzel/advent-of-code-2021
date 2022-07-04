with open("day_06.in", "rt") as f:
    puzzle_input = [int(age) for age in f.read().strip().split(",")]


def solve(days_to_go):
    # Keep track of how many fishes have given timer value
    tracker = [0] * (8 + 1)

    # Get initial state
    for fish_timer in puzzle_input:
        tracker[fish_timer] += 1

    for _ in range(days_to_go):

        # How many fish is about to spawn and reset
        zero_buffer = tracker[0]

        # Move the timers down
        for timer_value in range(8):
            tracker[timer_value] = tracker[timer_value + 1]

        tracker[8] = zero_buffer  # Spawn new fish
        tracker[6] += zero_buffer  # Reset

    fish_count = sum(tracker)
    print(f"{fish_count = }")


solve(80)  # Part 1
solve(256)  # Part 2
