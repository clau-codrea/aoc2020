import sys


def count_arrangements(adapters):
    adapters.sort()

    arrangements = 0
    mask = [None] * (len(adapters) - 1) + [1]

    def check_differences(mask, index):
        if not mask[index]:
            previous = 0
            for previous_index in range(index - 1, -1, -1):
                if mask[previous_index]:
                    previous = adapters[previous_index]
                    break

            if adapters[index + 1] - previous <= 3:
                return True

            return False

        return True

    def generate_masks(index):
        nonlocal arrangements

        if index == len(adapters) - 1:
            arrangements += 1
        else:
            for choice in range(2):
                mask[index] = choice
                if not check_differences(mask, index):
                    continue
                generate_masks(index + 1)

    generate_masks(0)

    return arrangements


def main(adapters_file_path):
    with open(adapters_file_path) as adapters_file:
        adapters = [int(line) for line in adapters_file]

    arrangements = count_arrangements(adapters)
    print(f"arrangements: {arrangements}")


if __name__ == "__main__":
    main(sys.argv[1])
