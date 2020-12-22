import sys


def next_token(expression, current_position):
    term = ""
    in_subexpression = False
    parentheses = 0
    while current_position < len(expression):
        current_character = expression[current_position]
        if in_subexpression:
            if current_character == "(":
                parentheses += 1
            elif current_character == ")":
                parentheses -= 1
                if not parentheses:
                    return term, current_position + 2

            term += current_character
            current_position += 1
        else:
            if current_character == " ":
                return term, current_position + 1
            elif current_character == "(":
                in_subexpression = True
                parentheses += 1
                current_position += 1
            else:
                term += current_character
                current_position += 1

    return term, current_position


def is_number(term):
    try:
        value = int(term)
    except ValueError:
        return False
    else:
        return True


def is_priority_operator(expression, current_position):
    while current_position < len(expression):
        current_character = expression[current_position]
        if current_character == "+":
            return True
        elif current_character == "*":
            return False

        current_position += 1

    return False


def compute(expression):
    factor, current_position = next_token(expression, 0)
    if is_number(factor):
        value = int(factor)
    else:
        value = compute(factor)
    while is_priority_operator(expression, current_position):
        op, current_position = next_token(expression, current_position)
        term, current_position = next_token(expression, current_position)
        if is_number(term):
            term_value = int(term)
        else:
            term_value = compute(term)

        value += term_value

    while current_position < len(expression):
        op, current_position = next_token(expression, current_position)
        factor, current_position = next_token(expression, current_position)
        if is_number(factor):
            second_value = int(factor)
        else:
            second_value = compute(factor)

        while is_priority_operator(expression, current_position):
            op, current_position = next_token(expression, current_position)
            term, current_position = next_token(expression, current_position)
            if is_number(term):
                term_value = int(term)
            else:
                term_value = compute(term)

            second_value += term_value

        value *= second_value

    return value


def main(expressions_file_path):
    total = 0
    with open(expressions_file_path) as expressions_file:
        for line in expressions_file:
            total += compute(line)

    print(f"total: {total}")


if __name__ == "__main__":
    main(sys.argv[1])
