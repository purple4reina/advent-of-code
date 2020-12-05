def load_passports(f):
    passports = []
    passport = {}
    for line in f:
        if line == '\n':
            passports.append(passport)
            passport = {}
        else:
            for item in line.strip().split(' '):
                k, v = item.split(':')
                passport[k] = v
    passports.append(passport)
    return passports


def main(f):
    required = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    optional = ('cid',)
    valid = 0
    for passport in load_passports(f):
        for k in required:
            if k not in passport:
                break
        else:
            valid += 1
    return valid


if __name__ == '__main__':
    with open('input.txt') as f:
        print(main(f))
