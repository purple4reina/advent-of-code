def solve(f):
    total = 0
    party = {}
    for row in f:
        row = row.strip()
        if not row:
            total += len(party)
            party.clear()
        else:
            for letter in row:
                party[letter] = True
    total += len(party)
    return total


if __name__ == '__main__':
    with open('input.txt') as f:
        print(solve(f))
