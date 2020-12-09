import sys
from collections import deque


def is_valid(number, numbers):
    for first_term in numbers:
        for second_term in numbers:
            if first_term == second_term:
                continue

            if number == first_term + second_term:
                return True

    return False


def find_invalid(numbers, encoded_file):
    all_numbers = []
    for line in encoded_file:
        number = int(line)

        if is_valid(number, numbers):
            all_numbers.append(numbers.popleft())
            numbers.append(number)
        else:
            all_numbers.extend(numbers)
            return number, all_numbers


def find_sequence(expected, numbers):
    sequence = deque(numbers[0:2])
    from_position = 2

    obtained = sum(sequence)
    while obtained != expected:
        if obtained > expected:
            sequence.popleft()
        else:
            sequence.append(numbers[from_position])
            from_position += 1

        obtained = sum(sequence)

    return sequence


def main(encoded_file_path):
    numbers = deque()
    with open(encoded_file_path) as encoded_file:
        for _ in range(25):
            line = encoded_file.readline()
            numbers.append(int(line))

        invalid, all_numbers = find_invalid(numbers, encoded_file)

    sequence = find_sequence(invalid, all_numbers)
    weakness = min(sequence) + max(sequence)

    print(f"invalid number: {invalid}")
    print(f"weakness: {weakness}")


if __name__ == "__main__":
    main(sys.argv[1])
