import sys


def run(operations):
    accumulator = 0
    position = 0
    previous_operations = set()

    finished = False

    while not finished:
        if position in previous_operations or not 0 <= position < len(operations):
            finished = True
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


def main(boot_file_path):
    with open(boot_file_path) as boot_file:
        operations = []

        for line in boot_file:
            operation, argument = line.split()
            operations.append((operation, int(argument)))

    accumulator = run(operations)
    print(f"Accumulator: {accumulator}")


if __name__ == "__main__":
    main(sys.argv[1])
