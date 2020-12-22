import sys
from collections import Counter


def main(forms_file_path):
    total = 0
    with open(forms_file_path) as forms_file:
        form, people = Counter(), 0
        for line in forms_file:
            questions = line.rstrip()

            if not questions:
                total += sum(1 if form[question] == people else 0 for question in form)
                form, people = Counter(), 0
            else:
                people += 1
                for question in questions:
                    form[question] += 1

        total += sum(1 if form[question] == people else 0 for question in form)

    print(f"Total: {total}")


if __name__ == "__main__":
    main(sys.argv[1])
