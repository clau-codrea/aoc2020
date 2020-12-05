import sys
from collections import namedtuple


def follow_directions(directions, count):
    lower, upper = 0, count - 1
    for direction in directions:
        if direction:
            lower = (lower + upper) // 2 + 1    
        else:
            upper = (lower + upper) // 2

    if lower == upper:
        return lower
    else:
        print('FUCK!!!')


def find_seat(boarding_pass, Seat):
    row_directions = [0 if direction == 'F' else 1 for direction in boarding_pass[:7]]
    column_directions = [0 if direction =='L' else 1 for direction in boarding_pass[7:]]

    return Seat(follow_directions(row_directions, 128), follow_directions(column_directions, 8))


def compute_id(seat):
    return seat.row * 8 + seat.column


def main(boarding_file_path):
    passes = []
    with open(boarding_file_path) as boarding_file:
        for line in boarding_file:
            passes.append(line.strip())

    Seat = namedtuple('Point', ['row', 'column'])

    highest_id = max(compute_id(find_seat(boarding_pass, Seat)) for boarding_pass in passes)
    print(f'Highest seat ID: {highest_id}')


if __name__ == '__main__':
    main(sys.argv[1])
