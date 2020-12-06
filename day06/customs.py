def solve(f):
    total = 0
    party = None
    for row in f:
        row = row.strip()
        person = set()
        if not row:
            total += len(party)
            party = None
        else:
            for letter in row:
                person.add(letter)
            if party == None:
                party = person
            else:
                party &= person
    total += len(party)
    return total


if __name__ == '__main__':
    with open('input.txt') as f:
        print(solve(f))
