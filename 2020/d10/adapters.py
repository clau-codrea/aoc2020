import sys
from math import prod, comb

d = {
    1: 2,
    2: 4,
    3: 1 + 3 + 3,
}


def count_arrangements(adapters):
    arrangements_count = 0

    arrangements = []

    current_count = -1
    index = 0
    while index < len(adapters) - 1:
        difference = adapters[index + 1] - adapters[index]
        if difference == 3:
            if current_count > 0:
                arrangements.append(
                    d[current_count]
                )  # comb(current_count + 1, current_count)) TODO???
            current_count = -1
        elif difference == 1:
            current_count += 1

        index += 1

    if current_count > 0:
        arrangements.append(d[current_count])

    arrangements_count = prod(arrangements)

    return arrangements_count


def main(adapters_file_path):
    with open(adapters_file_path) as adapters_file:
        adapters = [0] + sorted(int(line) for line in adapters_file)

    arrangements = count_arrangements(adapters)
    print(f"arrangements: {arrangements}")


if __name__ == "__main__":
    main(sys.argv[1])
