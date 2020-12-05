import sys
from collections import namedtuple


def follow_directions(directions, count):
    lower, upper = 0, count - 1
    for direction in directions:
        if direction:
            lower = (lower + upper) // 2 + 1
        else:
            upper = (lower + upper) // 2

    return lower


def find_seat(boarding_pass, Seat):
    row_directions = [0 if direction == "F" else 1 for direction in boarding_pass[:7]]
    column_directions = [
        0 if direction == "L" else 1 for direction in boarding_pass[7:]
    ]

    return Seat(
        follow_directions(row_directions, 128), follow_directions(column_directions, 8)
    )


def compute_id(seat):
    return seat.row * 8 + seat.column


def main(boarding_file_path):
    passes = []
    with open(boarding_file_path) as boarding_file:
        for line in boarding_file:
            passes.append(line.strip())

    Seat = namedtuple("Point", ["row", "column"])

    seat_ids = [compute_id(find_seat(boarding_pass, Seat)) for boarding_pass in passes]
    real_first, real_last = min(seat_ids), max(seat_ids)

    last_seat, last_front_missing, first_back_missing = (
        128 * 8 - 1,
        real_first - 1,
        real_last + 1,
    )

    front_missing_sum = last_front_missing * (last_front_missing + 1) // 2
    back_missing_sum = (
        first_back_missing * (last_seat - first_back_missing + 1)
        + (last_seat - first_back_missing) * (last_seat - first_back_missing + 1) // 2
    )
    total_sum = last_seat * (last_seat + 1) // 2

    real_total_sum = total_sum - front_missing_sum - back_missing_sum
    seat_id = real_total_sum - sum(seat_ids)

    print(f"Seat ID: {seat_id}")


if __name__ == "__main__":
    main(sys.argv[1])
