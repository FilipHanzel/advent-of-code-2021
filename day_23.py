from functools import lru_cache


with open("day_23.in", "rt") as f:
    rooms = [[], [], [], []]

    for line in f.readlines()[2:4]:
        for amphipod, room in zip(line.strip(" #\n").split("#"), rooms):
            if amphipod == "A":
                room.append(0)
            if amphipod == "B":
                room.append(1)
            if amphipod == "C":
                room.append(2)
            if amphipod == "D":
                room.append(3)

    rooms = tuple(map(tuple, rooms))

hall = (-1,) * 11

# All spaces are either empty (set to -1) or occupied by amphipod
# (set to index of a room given amphipod belongs to: A=0, B=1, C=2, D=3)


def get_cost(amphipod_type):
    if amphipod_type == 0:
        return 1
    if amphipod_type == 1:
        return 10
    if amphipod_type == 2:
        return 100
    if amphipod_type == 3:
        return 1000


def swap_tuple_value(to_be_swapped, index, new_value):
    to_be_swapped = list(to_be_swapped)
    to_be_swapped[index] = new_value
    return tuple(to_be_swapped)


def solve(rooms, hall):
    banned_hall_positions = [2, 4, 6, 8]

    min_cost = float("inf")

    @lru_cache(maxsize=None)
    def recurse(
        rooms,
        hall,
        cost=0,
    ):
        nonlocal min_cost

        if cost >= min_cost:
            return None

        if (
            rooms[0].count(0) == len(rooms[0])
            and rooms[1].count(1) == len(rooms[1])
            and rooms[2].count(2) == len(rooms[2])
            and rooms[3].count(3) == len(rooms[3])
        ):
            min_cost = min(min_cost, cost)
            return

        # Check all possible moves from a room to the hall

        for room_idx, room in enumerate(rooms):

            # If there is an amphipod to move in a given room
            if not room.count(-1) + room.count(room_idx) == len(room):
                to_move = room.count(-1)
                hall_index_outside_room = room_idx * 2 + 2
                amphipod = room[to_move]

                # Check if there are positions in the hall where
                # an amphipod can move
                possible_positions = []
                for position in range(len(hall)):
                    if position in banned_hall_positions:
                        continue

                    if hall[position] == -1:
                        possible_positions.append(position)
                    else:
                        # Do not include positions that are blocked
                        # by amphipod standing on the way
                        if position < hall_index_outside_room:
                            possible_positions.clear()
                        else:
                            break

                if possible_positions:
                    new_room = swap_tuple_value(room, to_move, -1)
                    new_rooms = swap_tuple_value(rooms, room_idx, new_room)

                    for position in possible_positions:
                        new_hall = swap_tuple_value(hall, position, amphipod)

                        distance = to_move + 1 + abs(position - hall_index_outside_room)
                        new_cost = cost + get_cost(amphipod) * distance

                        recurse(new_rooms, new_hall, new_cost)

        # Check all possible moves from the hall to the rooms

        for position in range(len(hall)):

            # If there is an amphipod to move
            if hall[position] != -1:
                room_idx = hall[position]
                room = rooms[room_idx]

                if room.count(-1) + room.count(room_idx) == len(room):
                    move_to = room.count(-1) - 1
                    hall_index_outside_room = room_idx * 2 + 2
                    amphipod = hall[position]

                    # Make sure there is no amphipod on the way
                    if position < hall_index_outside_room:
                        path = hall[position + 1 : hall_index_outside_room]
                    else:
                        path = hall[hall_index_outside_room:position]

                    if path.count(-1) < len(path):
                        continue

                    new_hall = swap_tuple_value(hall, position, -1)
                    new_room = swap_tuple_value(room, move_to, amphipod)
                    new_rooms = swap_tuple_value(rooms, room_idx, new_room)

                    distance = move_to + 1 + abs(position - hall_index_outside_room)
                    new_cost = cost + get_cost(amphipod) * distance

                    recurse(new_rooms, new_hall, new_cost)

    recurse(rooms, hall)
    return min_cost


# Part 1

min_cost = solve(rooms, hall)
print(f"{min_cost = }")

# Part 2

expanded_rooms = list(map(list, rooms))
expanded_rooms[0][1:1] = [3, 3]
expanded_rooms[1][1:1] = [2, 1]
expanded_rooms[2][1:1] = [1, 0]
expanded_rooms[3][1:1] = [0, 2]
expanded_rooms = tuple(map(tuple, expanded_rooms))

min_cost = solve(expanded_rooms, hall)
print(f"{min_cost = }")
