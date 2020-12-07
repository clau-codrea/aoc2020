import sys
import re


def read_rules(bags_file):
    contains = {}

    line_pattern = re.compile(
        "\A(?P<parent_color>[a-z]+ [a-z]+)(?: bags contain )(?P<children_colors>.+)\s\Z"
    )
    bag_pattern = re.compile("(?P<number>\A[0-9]+) (?P<color>[a-z]+ [a-z]+) bag")
    for line in bags_file:
        line_match = line_pattern.match(line)
        if line_match:
            parent_color = line_match.group("parent_color")
            children_bags = line_match.group("children_colors").split(", ")

            for bag in children_bags:
                bag_match = bag_pattern.match(bag)
                if bag_match:
                    child_color = bag_match.group("color")
                    child_number = int(bag_match.group("number"))
                    if parent_color in contains:
                        contains[parent_color][child_color] = child_number
                    else:
                        contains[parent_color] = {child_color: child_number}

    return contains


def get_contents(bag, bag_rules):
    contents = 0
    if bag not in bag_rules:
        return contents

    for child in bag_rules[bag]:
        contents += bag_rules[bag][child] * (1 + get_contents(child, bag_rules))

    return contents


def main(bags_file_path):
    with open(bags_file_path) as bags_file:
        bag_rules = read_rules(bags_file)

    bag = "shiny gold"
    contents = get_contents(bag, bag_rules)

    print(f"Bags inside {bag}: {contents}")


if __name__ == "__main__":
    main(sys.argv[1])
