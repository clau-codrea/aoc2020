import sys
import re


TERMINALS = ("a", "b")


def read(rules_file):
    reading_messages = False

    rules, messages = {}, []
    for line in rules_file:
        line = line.rstrip()

        if not line:
            reading_messages = True
        elif reading_messages:
            messages.append(line)
        else:
            rule_name, rule = line.split(": ")
            rule = rule.strip('"')
            options = rule.split(" | ")
            formatted_rule = []
            for option in options:
                references = [
                    int(x) if x not in TERMINALS else x for x in option.split()
                ]
                formatted_rule.append(references)
            rules[int(rule_name)] = formatted_rule

    return rules, messages


def all_words(grammar, start):
    words = set()

    candidates = [([start], 0)]

    while candidates:
        candidate, index = candidates.pop()

        if index >= len(candidate):
            if "".join(candidate) not in words:
                words.add("".join(candidate))
        else:
            options = grammar[candidate[index]]
            for option in options:
                new_candidate = candidate[:index] + option + candidate[index + 1 :]
                new_index = index + 1 if option[0] in TERMINALS else index
                candidates.append((new_candidate, new_index))

    return words


def count_valid_messages(messages, words):
    count = 0

    for message in messages:
        if message in words:
            count += 1

    return count


def main(rules_file_path):
    with open(rules_file_path) as rules_file:
        grammar, messages = read(rules_file)

    words = all_words(grammar, 0)

    valid_count = count_valid_messages(messages, words)
    print(f"count: {valid_count}")


if __name__ == "__main__":
    main(sys.argv[1])
