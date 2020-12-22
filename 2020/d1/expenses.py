import sys


def main(expenses_file_name):

    expenses = set()

    with open(expenses_file_name) as expenses_file:
        for line in expenses_file:
            expenses.add(int(line))

    for first_expense in expenses:
        for second_expense in expenses:
            if first_expense != second_expense:
                third_expense = 2020 - first_expense - second_expense
                if third_expense in expenses:
                    product = first_expense * second_expense * third_expense
                    print(
                        f"{first_expense} x {second_expense} x {third_expense} = {product}"
                    )
                    return


if __name__ == "__main__":
    main(sys.argv[1])
