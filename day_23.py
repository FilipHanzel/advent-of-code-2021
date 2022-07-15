from pprint import pprint

# TODO: Read from file

# Encode types as numbers
#
# A = 0
# B = 1
# C = 2
# D = 3
# Empty = -1
#
rooms = [
    [1, 3],
    [0, 0],
    [1, 3],
    [2, 2],
]

#    .----------------------.
#   | 0 1 2 3 4 5 6 7 8 9 A |
#   '---- B | C | B | D ---'
#       | A | D | C | A |
#       '--------------'

# room_exit_index = room_index * 2 + 2
#
hall = [-1] * 10
banned_hall_positions = [2, 4, 6, 8]


def get_cost(amphipod_type):
    if amphipod_type == 0:
        return 1
    if amphipod_type == 1:
        return 10
    if amphipod_type == 2:
        return 100
    if amphipod_type == 3:
        return 1000


min_cost = float("inf")

# TODO: Pass state here and add cache
def recurse(cost=0, history=[]):
    global min_cost
    if cost >= min_cost:
        return

    if (
        rooms[0][0] == 0
        and rooms[0][1] == 0
        and rooms[1][0] == 1
        and rooms[1][1] == 1
        and rooms[2][0] == 2
        and rooms[2][1] == 2
        and rooms[3][0] == 3
        and rooms[3][1] == 3
    ):
        min_cost = min(min_cost, cost)
        print(min_cost)
        pprint(history)
        return

    # Try all possible rooms
    for room_idx, room in enumerate(rooms):
        # Figure out which amphipod to move

        # If there is no one on top
        if room[0] == -1:
            # If there is no one on the bottom
            # or the one on the bottom is already in the correct room
            if room[1] == -1 or room[1] == room_idx:
                to_move = None
            else:
                to_move = 1
        else:
            # If the one on the bottom  and on top is already in the correct room
            if room[1] == room_idx and room[0] == room_idx:
                to_move = None
            else:
                to_move = 0

        # If there is an amphipod to move
        if to_move is not None:

            # Figure out to what position in the hall it can be moved to
            possible_positions = []
            for position in range(10):
                if position in banned_hall_positions:
                    continue

                # If space is free - amphipod can move there
                if hall[position] == -1:
                    possible_positions.append(position)
                # If space is not free
                else:
                    if position < room_idx * 2 + 2:
                        # space on the left of the room
                        possible_positions.clear()
                    else:  # Space on the right of the room
                        break

            # Try out all those possible positions
            amphipod_type, room[to_move] = room[to_move], -1

            for position in possible_positions:
                hall[position] = amphipod_type

                distance = to_move + 1 + abs(position - (room_idx * 2 + 2))
                added_cost = get_cost(amphipod_type) * distance
                history.append(
                    f"amphipod {amphipod_type} moved from room {room_idx}, to hall to position {position}"
                )
                recurse(cost + added_cost, history)
                history.pop()
                hall[position] = -1

            room[to_move] = amphipod_type

    # Check if amphipod can move into the room
    for position in range(10):
        if hall[position] != -1:
            amphipod_type = hall[position]
            room_idx = amphipod_type
            room = rooms[amphipod_type]

            move_to = None
            if room[0] == -1:
                if room[1] == -1:
                    move_to = 1
                elif room[1] == amphipod_type:
                    move_to = 0

            if move_to is not None:
                # Check if there is amphipod on the way
                if position < room_idx * 2 + 2:
                    # If amphipod is on the left of the room
                    path = hall[position + 1 : room_idx * 2 + 2]
                    if path.count(-1) < len(path):
                        continue
                else:
                    # If amphipod is on the right of the room
                    path = hall[room_idx * 2 + 2 : position]
                    if path.count(-1) < len(path):
                        continue

                hall[position], room[move_to] = -1, amphipod_type

                distance = move_to + 1 + abs(position - (room_idx * 2 + 2))
                added_cost = get_cost(amphipod_type) * distance

                history.append(
                    f"amphipod {amphipod_type} moved from hall {position}, to room {room_idx}"
                )
                recurse(cost + added_cost, history)
                history.pop()

                hall[position], room[move_to] = amphipod_type, -1


recurse()
print(f"{min_cost = }")
