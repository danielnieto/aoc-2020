import re

def read_passports():
    passports = []
    passport = ''

    with open('day4-input', 'r') as f:
        for line in f:
            passport += line
            if line == '\n':
                passports.append(passport.replace('\n', ' ').strip())
                passport = ''

        if passport:
            passports.append(passport)

    return passports

def parse_fields(passport):
    parsed = {}

    for pair in passport.split():
        key, value = pair.split(':')
        parsed[key] = value

    return parsed

def validate_hgt(v):

    if not v.endswith('cm') and not v.endswith('in'):
        return False

    num = int(v[:-2])

    if v.endswith('cm'):
        return num >= 150 and num <= 193
    return num >= 59 and num <= 76

def validate_byr(v):
    num = int(v)
    if len(v) == 4 and num >= 1920 and num <= 2002:
        return True

    print('byr', v)
    return False

def validate_iyr(v):
    num = int(v)
    return len(v) == 4 and num >= 2010 and num <= 2020

def validate_eyr(v):
    num = int(v)
    return len(v) == 4 and num >= 2020 and num <= 2030

def validate_hcl(v):
    pattern = re.compile("^#[0-9a-f]{6}$")

    if pattern.match(v) is None:
        return False

    return True

def validate_ecl(v):
    pattern = re.compile("^(amb|blu|brn|gry|grn|hzl|oth)$")

    if not pattern.match(v):
        return False

    return True

def validate_pid(v):
    pattern = re.compile("^[0-9]{9}$")

    if not pattern.match(v):
        return False

    return True

def is_valid(passport):
    required_fields = [
        ('byr', validate_byr),
        ('iyr', validate_iyr),
        ('eyr', validate_eyr),
        ('hgt', validate_hgt),
        ('hcl', validate_hcl),
        ('ecl', validate_ecl),
        ('pid', validate_pid)
    ]

    parsed_fields = parse_fields(passport)

    for field in required_fields:

        fid = field[0]

        if fid not in passport:
            return False

        validate_fn = field[1]
        if not validate_fn(parsed_fields[fid]):
            return False

    return True


if __name__ == "__main__":
    passports = read_passports()

    print(len(list(filter(lambda p: is_valid(p), passports))))

