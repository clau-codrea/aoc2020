import sys
import re


def parse(tickets_file):
    at_my_ticket = False
    at_nearby_tickets = False

    rule_pattern = re.compile(
        "\A(?P<rule>\w+( \w+)?): (?P<first_lower>\d+)-(?P<first_upper>\d+) or (?P<second_lower>\d+)-(?P<second_upper>\d+)\Z"
    )

    rules = {}
    nearby_tickets = []
    for line in tickets_file:
        line = line.rstrip()
        if not line:
            continue
        elif "your" in line:
            at_my_ticket = True
        elif "nearby" in line:
            at_my_ticket = False
            at_nearby_tickets = True
        elif at_my_ticket:
            my_ticket = [int(number) for number in line.split(",")]
        elif at_nearby_tickets:
            nearby_tickets.append([int(number) for number in line.split(",")])
        else:
            rule_match = rule_pattern.match(line)
            rule_name = rule_match.group("rule").replace(" ", "_")
            first_lower, first_upper, second_lower, second_upper = (
                int(value)
                for value in rule_match.group(
                    "first_lower", "first_upper", "second_lower", "second_upper"
                )
            )
            rules[rule_name] = (
                (first_lower, first_upper),
                (second_lower, second_upper),
            )

    return rules, my_ticket, nearby_tickets


def valid(value, rules):
    for first_range, second_range in rules.values():
        if (
            first_range[0] <= value <= first_range[1]
            or second_range[0] <= value <= second_range[1]
        ):
            return True

    return False


def scan_ticket(ticket, rules, positions):
    for value in ticket:
        if not valid(value, rules):
            return

    for rule in rules:
        first_range, second_range = rules[rule]

        for index, value in enumerate(ticket):
            if not (
                first_range[0] <= value <= first_range[1]
                or second_range[0] <= value <= second_range[1]
            ):
                positions[rule].add(index)


def scan_tickets(tickets, rules):
    positions = {rule_name: set() for rule_name in rules.keys()}
    for ticket in tickets:
        scan_ticket(ticket, rules, positions)

    return positions


def format_fields(invalid_positions):
    positions = {}
    for field in invalid_positions:
        positions[field] = set(range(len(invalid_positions))) - invalid_positions[field]

    fields = {}
    for field in positions:
        for position in positions[field]:
            if position in fields:
                fields[position].add(field)
            else:
                fields[position] = {field}

    return fields


def find_positions(positions):
    solution = [None for _ in range(len(positions))]
    final = None

    def is_candidate(index):
        for field in solution[:index]:
            if field == solution[index]:
                return False

        return True

    def backtrack(index):
        if index == len(solution):
            if is_candidate(len(solution) - 1):
                nonlocal final
                final = solution[:]
            return

        for field in positions[index]:
            solution[index] = field
            if is_candidate(index):
                backtrack(index + 1)

    backtrack(0)

    return final


def compute_departures_product(ticket, ordered_fields):
    product = 1

    for index, field in enumerate(ordered_fields):
        if "departure" in field:
            product *= ticket[index]

    return product


def main(tickets_file_path):
    with open(tickets_file_path) as tickets_file:
        rules, my_ticket, nearby_tickets = parse(tickets_file)

    invalid_positions = scan_tickets(nearby_tickets, rules)
    fields = format_fields(invalid_positions)
    ordered_fields = find_positions(fields)
    result = compute_departures_product(my_ticket, ordered_fields)
    print(f"result: {result}")


if __name__ == "__main__":
    main(sys.argv[1])
