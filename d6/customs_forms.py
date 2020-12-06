import sys


def main(forms_file_path):
    total = 0
    with open(forms_file_path) as forms_file:
        form = set()
        for line in forms_file:
            questions = line.rstrip()

            if not questions:
                total += len(form)
                form = set()

            for question in questions:
                form.add(question)

        total+= len(form)

    print(f'Total: {total}')


if __name__ == '__main__':
    main(sys.argv[1])
