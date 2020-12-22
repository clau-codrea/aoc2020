import sys
import re


def obtain(passports_file):
    passport = {}

    complete = False
    while not complete:
        line = passports_file.readline()
        if not line:
            if passport:
                return passport
            else:
                return
        if not line.strip():
            complete = True
        fields = line.split()
        for field in fields:
            name, value = field.split(":")
            passport[name] = value

    return passport


def valid_year(byr, lower, upper):
    if not re.match("\A[0-9]{4}\Z", byr):
        return False

    return lower <= int(byr) <= upper


def valid_height(hgt):
    match = re.match("\A([1-9][0-9]*)(cm|in)\Z", hgt)
    if not match:
        return False

    height, unit = match.groups()
    if unit == "cm":
        lower, upper = 150, 193
    else:
        lower, upper = 59, 76
    return lower <= int(height) <= upper


def valid_hair_color(hcl):
    return re.match("\A#[0-9a-f]{6}\Z", hcl)


def valid_eye_color(ecl):
    return ecl in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")


def valid_passport_id(pid):
    return re.match("\A[0-9]{9}\Z", pid)


def valid(passport):
    required_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")

    return (
        all(field in passport for field in required_fields)
        and valid_year(passport["byr"], 1920, 2002)
        and valid_year(passport["iyr"], 2010, 2020)
        and valid_year(passport["eyr"], 2020, 2030)
        and valid_height(passport["hgt"])
        and valid_hair_color(passport["hcl"])
        and valid_eye_color(passport["ecl"])
        and valid_passport_id(passport["pid"])
    )


def main(passports_file_path):
    valid_passports = 0
    finished = False
    with open(passports_file_path) as passports_file:
        while not finished:
            passport = obtain(passports_file)
            if not passport:
                finished = True
            else:
                if valid(passport):
                    valid_passports += 1

    print(f"Valid passports: {valid_passports}")


if __name__ == "__main__":
    main(sys.argv[1])
