import sys


def run(operations):
    accumulator = 0
    position = 0
    previous_operations = set()

    finished = False

    while not finished:
        if position == len(operations):
            finished = True
        elif position in previous_operations:
            return -1
        else:
            previous_operations.add(position)
            operation, argument = operations[position]

            if operation == "nop":
                position += 1
            elif operation == "acc":
                accumulator += argument
                position += 1
            elif operation == "jmp":
                position += argument

    return accumulator


def check(operations):
    finished = False
    position = 0
    while not finished:
        if operations[position][0] == "acc":
            position += 1
            continue

        operations[position][0] = "nop" if operations[position][0] == "jmp" else "jmp"

        accumulator = run(operations)

        if accumulator != -1:
            finished = True

        operations[position][0] = "nop" if operations[position][0] == "jmp" else "jmp"

        position += 1

    return accumulator


def main(boot_file_path):
    with open(boot_file_path) as boot_file:
        operations = []

        for line in boot_file:
            operation, argument = line.split()
            operations.append([operation, int(argument)])

    accumulator = check(operations)

    print(f"Accumulator: {accumulator}")


if __name__ == "__main__":
    main(sys.argv[1])
