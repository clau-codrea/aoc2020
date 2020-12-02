import sys
import re

def is_valid(match):
    lower = int(match.group('lower'))
    upper = int(match.group('upper'))
    letter, password = match.group('letter', 'password')

    if lower <= password.count(letter) <= upper:
        return True

    return False
    
def main():
    file_name = sys.argv[1] 

    pattern = re.compile('\A(?P<lower>[0-9]+)-(?P<upper>[0-9]+)\s(?P<letter>[a-z]):\s(?P<password>[a-z]+)\s*\Z')

    valid = 0
    with open(file_name) as passwords_file:
        for line in passwords_file:
            match = pattern.match(line)
            if match and is_valid(match):
                valid += 1

    print(f'Valid passwords: {valid}')


if __name__ == '__main__':
    main()
