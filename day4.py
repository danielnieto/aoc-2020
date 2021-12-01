
def read_passports():
    passports = []
    passport = ''

    with open('day4-input', 'r') as f:
        for line in f:
            passport += line
            if line == '\n':
                passports.append(passport.replace('\n', ' ').strip())
                passport = ''

    return passports

def is_valid(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    for field in required_fields:
        if field not in passport:
            return False
    return True


if __name__ == "__main__":
    passports = read_passports()
    print(len(list(filter(lambda p: is_valid(p), passports))))

