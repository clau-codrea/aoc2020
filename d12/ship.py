import sys
import re


CARDINAL_POINTS = ('N', 'E', 'S', 'W')


def read_instructions(instructions_file):
    instructions_pattern = re.compile('\A([NSEWLRF])([1-9][0-9]*)\s\Z')

    return [instructions_pattern.match(line).groups() for line in instructions_file]


def process_instruction(instruction, initial_position, initial_orientation):
    def process_cardinal_point(instruction):
        if instruction[0] == 'E':
            return 1, 0
        elif instruction[0] == 'W':
            return -1, 0
        elif instruction[0] == 'N':
            return 1, 1
        else:
            return -1, 1


    def process_orientation(instruction):
        offset = int(instruction[1]) // 90
        if instruction[0] == 'L':
            return -1, offset
        else:
            return 1, offset

    
    x, y = initial_position
    orientation = initial_orientation

    if instruction[0] in ('L', 'R'):
        coefficient, offset = process_orientation(instruction)
        index = CARDINAL_POINTS.index(initial_orientation)

        while offset:
            index += coefficient
            if index == -1:
                index = len(CARDINAL_POINTS) - 1
            elif index == len(CARDINAL_POINTS):
                index = 0

            offset -= 1

        orientation = CARDINAL_POINTS[index]
    else:
        if instruction[0] == 'F':
            instruction = (orientation, instruction[1])
       
        coefficient, axis = process_cardinal_point(instruction)
        increment = coefficient * int(instruction[1])
        if axis:
            y += increment
        else:
            x += increment

    return (x, y), orientation


def follow(instructions):
    position = (0, 0)
    orientation = 'E'

    for instruction in instructions:
        position, orientation = process_instruction(instruction, position, orientation)
    return position


def compute_manhattan_distance(position):
    return abs(position[0]) + abs(position[1])


def main(instructions_file_path):
    with open(instructions_file_path) as instructions_file:
        instructions = read_instructions(instructions_file)

    position = follow(instructions)
    manhattan_distance = compute_manhattan_distance(position)

    print(f'md: {manhattan_distance}')


if __name__ == '__main__':
    main(sys.argv[1])
