import sys
import re


def to_binary(value):
    binary_value = ""
    remainders = []
    while value:
        remainders.append(value % 2)
        value //= 2

    return "".join(str(x) for x in reversed(remainders)).rjust(36, "0")


def to_decimal(value):
    decimal_value = 0
    power = 1

    for symbol in reversed(value):
        decimal_value += int(symbol) * power
        power *= 2

    return decimal_value


def apply_mask(value, mask):
    actual_value = ""
    for value_symbol, mask_symbol in zip(value, mask):
        if mask_symbol != "X":
            actual_value += mask_symbol
        else:
            actual_value += value_symbol

    return actual_value


def update_memory(memory, memory_location, memory_value, mask):
    binary_value = to_binary(memory_value)
    actual_value = apply_mask(binary_value, mask)
    memory[memory_location] = to_decimal(actual_value)


def process(memory_file):
    memory = {}

    mask_pattern = re.compile("\Amask = ([X01]{36})\Z")
    memory_pattern = re.compile("\Amem\[(\d+)\] = (\d+)\Z")

    mask = ""

    for line in memory_file:
        line = line.rstrip()
        mask_match = mask_pattern.match(line)
        if mask_match:
            mask = mask_match.group(1)
        else:
            memory_match = memory_pattern.match(line)
            memory_location, memory_value = (int(x) for x in memory_match.groups())
            update_memory(memory, memory_location, memory_value, mask)

    return memory


def main(memory_file_path):
    with open(memory_file_path) as memory_file:
        memory = process(memory_file)

    total = sum(memory.values())
    print(f"total: {total}")


if __name__ == "__main__":
    main(sys.argv[1])
