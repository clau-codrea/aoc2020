import sys


def look_for_trees(slopes_file):
    line = slopes_file.readline().rstrip()
    columns = len(line)
    slopes_file.seek(0)

    trees = []
    for line in slopes_file:
        tree_line = set()

        for position, square in enumerate(line):
            if square == "#":
                tree_line.add(position)

        trees.append(tree_line)

    return trees, columns


def descend(right, down, trees, columns):
    row, column, hits = 0, 0, 0
    while row < len(trees):
        if column in trees[row]:
            hits += 1
        row += down
        column += right
        column %= columns

    return hits


def main(slopes_file_name):
    with open(slopes_file_name) as slopes_file:
        trees, columns = look_for_trees(slopes_file)

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    hits = 1
    for right, down in slopes:
        hits *= descend(right, down, trees, columns)

    print(f"Total hits: {hits}")


if __name__ == "__main__":
    main(sys.argv[1])
