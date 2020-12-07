import sys
import re


def read_rules(bags_file):
    parents = {}

    line_pattern = re.compile(
        "\A(?P<parent_color>[a-z]+ [a-z]+)(?: bags contain )(?P<children_colors>.+)\s\Z"
    )
    bag_pattern = re.compile("\A[0-9]+ (?P<color>[a-z]+ [a-z]+) bag")
    for line in bags_file:
        line_match = line_pattern.match(line)
        if line_match:
            parent_color = line_match.group("parent_color")
            children_bags = line_match.group("children_colors").split(", ")

            for bag in children_bags:
                bag_match = bag_pattern.match(bag)
                if bag_match:
                    child_color = bag_match.group("color")
                    if child_color in parents:
                        parents[child_color].add(parent_color)
                    else:
                        parents[child_color] = {parent_color}

    return parents


def all_ancestors(bag, bag_rules):
    ancestors = set()
    if bag not in bag_rules:
        return ancestors

    for parent in bag_rules[bag]:
        ancestors.add(parent)
        ancestors.update(all_ancestors(parent, bag_rules))

    return ancestors


def main(bags_file_path):
    with open(bags_file_path) as bags_file:
        bag_rules = read_rules(bags_file)

    bag = "shiny gold"
    bags_containing = all_ancestors(bag, bag_rules)

    print(f"Bags that can contain {bag}: {len(bags_containing)}")


if __name__ == "__main__":
    main(sys.argv[1])
