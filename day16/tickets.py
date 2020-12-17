def parse(inp):
    section = 0
    skip = False
    ranges = {'all': {}}
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
            field, nums = line.split(': ')
            ranges[field] = {}
            for r in nums.split(' or '):
                bottom, top = map(int, r.split('-'))
                for n in range(bottom, top + 1):
                    ranges[field][n] = True
                    ranges['all'][n] = True
        elif section == 1:
            myticket = tuple(map(int, line.split(',')))
        else:
            tickets.append(tuple(map(int, line.split(','))))
    return ranges, myticket, tickets


def solve(inp):
    ranges, myticket, tickets = parse(inp)
    possibles = {i: {} for i in range(len(tickets[0]))}
    for ticket in tickets:
        for i, val in enumerate(ticket):
            if not ranges['all'].get(val):
                break
            for field, rngs in ranges.items():
                if not rngs.get(val):
                    possibles[i][field] = False

    del ranges['all']
    fields = len(ranges)
    key = {}

    while possibles:
        for i, pos in list(possibles.items()):
            if len(pos) == fields - 1:
                for field in ranges:
                    if field not in pos:
                        key[field] = i
                        del possibles[i]
                        del ranges[field]
                        fields -= 1
                        for p in possibles.values():
                            if field in p:
                                del p[field]
                        break

    prod = 1
    for k, v in key.items():
        if k.startswith('departure'):
            prod *= myticket[v]
    return prod


if __name__ == '__main__':
    with open('input.txt') as f:
        print(solve(f))
