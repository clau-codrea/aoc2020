import sys


def count_differences(adapters):
    differences = {1: 0, 3: 1}
    previous = 0
    for adapter in adapters:
        differences[adapter - previous] += 1
        previous = adapter

    return differences


def main(adapters_file_path):
    adapters = []
    with open(adapters_file_path) as adapters_file:
        for line in adapters_file:
            adapters.append(int(line))

    differences = count_differences(sorted(adapters))
    jolts = differences[1] * differences[3]
    print(f"jolts: {jolts}")


if __name__ == "__main__":
    main(sys.argv[1])
