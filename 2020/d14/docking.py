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


def apply_mask(memory_location, mask):
    actual_memory_location = ""
    for memory_symbol, mask_symbol in zip(memory_location, mask):
        if mask_symbol in ("X", "1"):
            actual_memory_location += mask_symbol
        else:
            actual_memory_location += memory_symbol

    return actual_memory_location


def generate_memory_locations(initial_memory_location):
    memory_locations = [initial_memory_location]

    done = False
    while not done:
        generated_memory_locations = []
        for memory_location in memory_locations:
            try:
                index = memory_location.index("X")
            except ValueError:
                done = True
            else:
                variants = [
                    memory_location[:index] + symbol + memory_location[index + 1 :]
                    for symbol in ("0", "1")
                ]
                generated_memory_locations.extend(variants)

                memory_locations = generated_memory_locations[:]

    return memory_locations


def update_memory(memory, memory_locations, memory_value):
    for memory_location in (to_decimal(x) for x in memory_locations):
        memory[memory_location] = memory_value

    return memory


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
            binary_memory_location = to_binary(memory_location)
            actual_memory_location = apply_mask(binary_memory_location, mask)
            memory_locations = generate_memory_locations(actual_memory_location)
            memory = update_memory(memory, memory_locations, memory_value)

    return memory


def main(memory_file_path):
    with open(memory_file_path) as memory_file:
        memory = process(memory_file)

    total = sum(memory.values())
    print(f"total: {total}")


if __name__ == "__main__":
    main(sys.argv[1])
