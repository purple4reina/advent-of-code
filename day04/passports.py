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


def validate_year(txt, minn, maxx):
    if not txt:
        return False
    if len(txt) != 4:
        return False
    try:
        year = int(txt)
    except:
        return False
    return year >= minn and year <= maxx

def byr(txt):
    return validate_year(txt, 1920, 2002)

def iyr(txt):
    return validate_year(txt, 2010, 2020)

def eyr(txt):
    return validate_year(txt, 2020, 2030)

def hgt(txt):
    if not txt:
        return False
    size = txt[:-2]
    try:
        num = int(size)
    except:
        return False
    if txt[-2:] == 'cm':
        return num >= 150 and num <= 193
    elif txt[-2:] == 'in':
        return num >= 59 and num <= 76
    return False

def hcl(txt):
    if not txt:
        return False
    if txt[0] != '#':
        return False
    if len(txt) != 7:
        return False
    try:
        int(txt[1:], 16)
        return txt.lower() == txt
    except:
        return False

def ecl(txt):
    return txt in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

def pid(txt):
    if not txt:
        return False
    if len(txt) != 9:
        return False
    try:
        num = int(txt)
        return True
    except:
        return False


validators = {
        'byr': byr,
        'iyr': iyr,
        'eyr': eyr,
        'hgt': hgt,
        'hcl': hcl,
        'ecl': ecl,
        'pid': pid,
}


def main(f):
    valid = 0
    for passport in load_passports(f):
        for k, validate in validators.items():
            if not validate(passport.get(k)):
                break
        else:
            valid += 1
    return valid


if __name__ == '__main__':
    with open('input.txt') as f:
        print(main(f))
