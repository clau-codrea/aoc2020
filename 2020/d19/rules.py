import sys
import re

from itertools import product


TERMINALS = ("a", "b")
START = 0


def read(rules_file):
    reading_messages = False

    rules, messages, complete, todo = {}, set(), {}, set()
    for line in rules_file:
        line = line.rstrip()

        if not line:
            reading_messages = True
        elif reading_messages:
            messages.add(line)
        else:
            rule_name, rule = line.split(": ")
            rule = rule.strip('"')
            options = rule.split(" | ")
            if len(options) == 1 and options[0] in TERMINALS:
                complete[int(rule_name)] = set(options[0])
            else:
                formatted_rule = []
                for option in options:
                    references = [int(x) for x in option.split()]
                    formatted_rule.append(references)
                rules[int(rule_name)] = formatted_rule
                todo.add(int(rule_name))

    del rules[8]
    todo.remove(8)
    del rules[11]
    todo.remove(11)

    rules[0] = [[42, 42, 31]]

    return rules, messages, complete, todo


def can_complete(rule, grammar, completed):
    for option in grammar[rule]:
        for subrule in option:
            if subrule not in completed:
                return False

    return True


def complete(rule, grammar, completed):
    completed[rule] = set()
    for option in grammar[rule]:
        completed_subrules = [completed[subrule] for subrule in option]
        completed_option = list(product(*completed_subrules))
        completed[rule].update("".join(x) for x in completed_option)


def complete_all(grammar, todo, completed):
    while START in todo:
        for rule in todo.copy():
            if can_complete(rule, grammar, completed):
                complete(rule, grammar, completed)
                todo.remove(rule)


def main(rules_file_path):
    with open(rules_file_path) as rules_file:
        grammar, messages, completed, todo = read(rules_file)

    complete_all(grammar, todo, completed)

    valid_count = len(completed[START] & messages)

    print(f"count: {valid_count}")


if __name__ == "__main__":
    main(sys.argv[1])
