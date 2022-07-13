from functools import lru_cache

with open("day_21.in", "rt") as f:
    position_1 = int(f.readline().strip()[-1]) - 1
    position_2 = int(f.readline().strip()[-1]) - 1

# Part 1

roll_counter = 0
turn_counter = 1


def roll():
    global roll_counter
    global turn_counter

    roll_counter += 3

    score = 0
    for _ in range(3):
        score += turn_counter
        turn_counter += 1
        if turn_counter > 100:
            turn_counter = 1
    return score


score_1 = 0
score_2 = 0
new_position_1 = position_1
new_position_2 = position_2

while score_1 < 1000 and score_2 < 1000:
    new_position_1 += roll()
    new_position_1 %= 10
    score_1 += new_position_1 + 1

    if score_1 >= 1000:
        break

    new_position_2 += roll()
    new_position_2 %= 10
    score_2 += new_position_2 + 1

    if score_2 >= 1000:
        break

loosing_score = min(score_1, score_2)

print(f"{roll_counter * loosing_score = }")

# Part 2

# Every 3 throws (single turn of one player) will create 27 universes
# In 1 of them sum of those 3 throws will be equal to 9
# In 3 of them sum of those 3 throws will be equal to 8
# In 6 of them sum of those 3 throws will be equal to 7
# In 7 of them sum of those 3 throws will be equal to 6
# In 6 of them sum of those 3 throws will be equal to 5
# In 3 of them sum of those 3 throws will be equal to 4
# In 1 of them sum of those 3 throws will be equal to 3
possible_throw_outcomes = {
    9: 1,
    8: 3,
    7: 6,
    6: 7,
    5: 6,
    4: 3,
    3: 1,
}


@lru_cache(maxsize=None)
def recurse(score_1, position_1, score_2, position_2):
    global possible_throw_outcomes

    wins_1 = wins_2 = 0

    original_position_1 = position_1
    original_position_2 = position_2

    original_score_1 = score_1
    original_score_2 = score_2

    for first in possible_throw_outcomes:
        # We could get here in possible_throw_outcomes[first] ways

        position_1 = (original_position_1 + first) % 10
        score_1 = original_score_1 + position_1 + 1
        if score_1 >= 21:
            wins_1 += possible_throw_outcomes[first]
            continue

        for second in possible_throw_outcomes:
            # We could get here in possible_throw_outcomes[second] * possible_throw_outcomes[first] ways
            mul = possible_throw_outcomes[second] * possible_throw_outcomes[first]

            position_2 = (original_position_2 + second) % 10
            score_2 = original_score_2 + position_2 + 1
            if score_2 >= 21:
                wins_2 += mul
                continue

            results = recurse(score_1, position_1, score_2, position_2)

            mul = possible_throw_outcomes[first] * possible_throw_outcomes[second]

            wins_1 += results[0] * mul
            wins_2 += results[1] * mul

    return wins_1, wins_2


player_1_wins, player_2_wins = recurse(0, position_1, 0, position_2)

print("Part 2")
print(f"{player_1_wins = }")
print(f"{player_2_wins = }")
