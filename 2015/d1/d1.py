def find_floor(instructions):
    return sum(1 if instruction == '(' else -1 for instruction in instructions)

def main():
    with open('input') as input_file:
        instructions = input_file.readline().rstrip()

    floor = find_floor(instructions)
    print(floor)

main()
