import sys


def count_arrangements(adapters):
    arrangements_count = 0

    arrangements = [(adapters, 1)]

    while arrangements:
        arrangements_count += len(arrangements)
        new_arrangements = []
        for arrangement, start_index in arrangements:
            for current_index in range(start_index, len(arrangement) - 1):
                if arrangement[current_index + 1] - arrangement[current_index - 1] <= 3:
                    new_arrangements.append(
                        (
                            arrangement[:current_index]
                            + arrangement[current_index + 1 :],
                            current_index,
                        )
                    )

        arrangements = new_arrangements

    return arrangements_count


def main(adapters_file_path):
    with open(adapters_file_path) as adapters_file:
        adapters = [0] + sorted(int(line) for line in adapters_file)

    arrangements = count_arrangements(adapters)
    print(f"arrangements: {arrangements}")


if __name__ == "__main__":
    main(sys.argv[1])
