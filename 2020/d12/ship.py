import sys
import re


CARDINAL_POINTS = ("N", "E", "S", "W")


def read_instructions(instructions_file):
    instructions_pattern = re.compile("\A([NSEWLRF])([1-9][0-9]*)\s\Z")

    return [instructions_pattern.match(line).groups() for line in instructions_file]


def process_instruction(instruction, initial_ship_position, initial_waypoint_position):
    def process_cardinal_point(instruction):
        if instruction[0] == "E":
            return 1, 0
        elif instruction[0] == "W":
            return -1, 0
        elif instruction[0] == "N":
            return 1, 1
        else:
            return -1, 1

    def process_orientation(instruction, waypoint_position):
        if instruction[0] == "R":
            x = waypoint_position[1]
            y = -waypoint_position[0]
        else:
            x = -waypoint_position[1]
            y = waypoint_position[0]

        return (x, y)

    ship_x, ship_y = initial_ship_position
    waypoint_x, waypoint_y = initial_waypoint_position

    if instruction[0] in ("L", "R"):
        for _ in range(int(instruction[1]) // 90):
            waypoint_x, waypoint_y = process_orientation(
                instruction, (waypoint_x, waypoint_y)
            )
    elif instruction[0] in CARDINAL_POINTS:
        coefficient, axis = process_cardinal_point(instruction)
        increment = coefficient * int(instruction[1])
        if axis:
            waypoint_y += increment
        else:
            waypoint_x += increment
    else:
        ship_x += int(instruction[1]) * waypoint_x
        ship_y += int(instruction[1]) * waypoint_y

    return (ship_x, ship_y), (waypoint_x, waypoint_y)


def follow(instructions):
    ship_position = (0, 0)
    waypoint_position = (10, 1)

    for instruction in instructions:
        ship_position, waypoint_position = process_instruction(
            instruction, ship_position, waypoint_position
        )
        print(ship_position, waypoint_position)
    return ship_position


def compute_manhattan_distance(position):
    return abs(position[0]) + abs(position[1])


def main(instructions_file_path):
    with open(instructions_file_path) as instructions_file:
        instructions = read_instructions(instructions_file)

    position = follow(instructions)
    manhattan_distance = compute_manhattan_distance(position)

    print(f"md: {manhattan_distance}")


if __name__ == "__main__":
    main(sys.argv[1])
