import sys


FLOOR = 0
EMPTY = 1
OCCUPIED = 2


def parse(seating_file):
    seating_area = []

    for line in seating_file:
        row = []
        for seat in line.rstrip():
            if seat == ".":
                row.append(FLOOR)
            elif seat == "L":
                row.append(EMPTY)
            else:
                row.append(OCCUPIED)
        seating_area.append(row)

    return seating_area


def get_adjacent(initial_row, initial_column, seating_area):
    dimensions = (len(seating_area), len(seating_area[0]))
    adjacent = []

    for row_offset in (-1, 0, 1):
        for column_offset in (-1, 0, 1):
            if row_offset == column_offset == 0:
                continue

            seen = False
            row_index, column_index = initial_row, initial_column
            while not seen:
                row_index += row_offset
                column_index += column_offset
                if (
                    row_index < 0
                    or row_index >= dimensions[0]
                    or column_index < 0
                    or column_index >= dimensions[1]
                ):
                    seen = True
                    continue

                element = seating_area[row_index][column_index]
                if element != FLOOR:
                    adjacent.append(element)
                    seen = True

    return adjacent


def next_state(current, adjacent_seats):
    state = current

    if state == EMPTY and all(
        (True if seat == EMPTY else False) for seat in adjacent_seats
    ):
        state = OCCUPIED
    elif state == OCCUPIED:
        adjacent_count = sum((1 if seat == OCCUPIED else 0) for seat in adjacent_seats)
        if adjacent_count >= 5:
            state = EMPTY

    return state


def generate_one(seating_area):
    new_state = {row: {} for row in range(len(seating_area))}
    switched = False

    for row_index, row in enumerate(seating_area):
        for column_index, seat in enumerate(row):
            adjacent = get_adjacent(row_index, column_index, seating_area)
            seat_next_state = next_state(seat, adjacent)
            if seat != seat_next_state:
                new_state[row_index][column_index] = seat_next_state
                switched = True

    return new_state, switched


def generate(seating_area):
    switched = True

    while switched:
        new_state, switched = generate_one(seating_area)
        if switched:
            for row in new_state:
                for column in new_state[row]:
                    seating_area[row][column] = new_state[row][column]

    return seating_area


def count_occupied(seating_area):
    occupied = 0

    for row in seating_area:
        for space in row:
            if space == OCCUPIED:
                occupied += 1

    return occupied


def main(seating_file_path):
    with open(seating_file_path) as seating_file:
        seating_area = parse(seating_file)

    seating_area = generate(seating_area)
    occupied = count_occupied(seating_area)

    print(f"occupied: {occupied}")


if __name__ == "__main__":
    main(sys.argv[1])
