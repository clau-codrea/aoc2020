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


def scan_ticket(ticket, rules):
    errors = 0

    for value in ticket:
        if not valid(value, rules):
            errors += value

    return errors


def scan_errors(tickets, rules):
    total_errors = 0
    for ticket in tickets:
        ticket_errors = scan_ticket(ticket, rules)
        total_errors += ticket_errors

    return total_errors


def main(tickets_file_path):
    with open(tickets_file_path) as tickets_file:
        rules, my_ticket, nearby_tickets = parse(tickets_file)

    errors = scan_errors(nearby_tickets, rules)
    print(f"errors: {errors}")


if __name__ == "__main__":
    main(sys.argv[1])
