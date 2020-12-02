import sys


def main(expenses_file_name):

    expenses = set()

    with open(expenses_file_name) as expenses_file:
        for line in expenses_file:
            expenses.add(int(line))

    for expense in expenses:
        if 2020 - expense in expenses:
            print(f"{expense} x {2020 - expense} = {expense * (2020 - expense)}")
            return


if __name__ == "__main__":
    main(sys.argv[1])
