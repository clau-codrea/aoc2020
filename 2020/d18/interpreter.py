import sys


def next_token(expression, current_position):
    term = ''
    while current_position < len(expression):
        if expression[current_position] == ' ':
            return term, current_position + 1
        else:
            term += expression[current_position]
            current_position += 1

    return term, current_position


def is_number(term):
    try:
        value = int(term)
    except ValueError:
        return False
    else:
        return True


def compute(expression):
    print(expression)
    term, current_position = next_token(expression, 0)
    if is_number(term):
        value = int(term)
    else:
        value = compute(term[1:-1])

    while current_position < len(expression):
        op, current_position = next_token(expression, current_position)
        term, current_position = next_token(expression, current_position)
        if is_number(term):
            second_value = int(term)
        else:
            second_value = compute(term[1:-1])
        if op == '+':
            value += second_value
        else:
            value *= second_value

    return value


def main(expressions_file_path):
    total = 0
    with open(expressions_file_path) as expressions_file:
        for line in expressions_file:
            total += compute(line)

    print(f'total: {total}')


if __name__ == '__main__':
    main(sys.argv[1])
