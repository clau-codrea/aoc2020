BASEMENT = -1

def reach_basement(instructions):
    floor = 0
    for index, instruction in enumerate(instructions):
        direction = 1 if instruction == '(' else -1
        floor += direction
        if floor == BASEMENT:
            return index + 1


def main():
    with open('input') as input_file:
        instructions = input_file.readline().rstrip()

    instruction_position = reach_basement(instructions)
    print(instruction_position)

main()
