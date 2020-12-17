def parse(inp):
    section = 0
    skip = False
    ranges = {}
    tickets = []
    for line in inp:
        if skip:
            skip = False
            continue
        line = line.strip()
        if not line:
            section += 1
            skip = True
            continue
        if section == 0:
            _, nums = line.split(': ')
            for r in nums.split(' or '):
                bottom, top = map(int, r.split('-'))
                for n in range(bottom, top + 1):
                    ranges[n] = True
        elif section == 1:
            pass
        else:
            tickets.append(map(int, line.split(',')))
    return ranges, tickets


def solve(inp):
    ranges, tickets = parse(inp)
    total = 0
    for ticket in tickets:
        for val in ticket:
            if not ranges.get(val):
                total += val
    return total


if __name__ == '__main__':
    with open('input.txt') as f:
        print(solve(f))
