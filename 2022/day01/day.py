def part1(inputs):
    top_e = this_e = 0
    for cals in inputs:
        this_e += cals
        if not cals:
            top_e, this_e = max(this_e, top_e), 0
    top_e, this_e = max(this_e, top_e), 0
    return top_e

def part2(inputs):
    vals, this_e = [], 0
    for cals in inputs:
        this_e += cals
        if not cals:
            vals.append(this_e)
            this_e = 0
    vals.append(this_e)
    return sum(sorted(vals)[-3:])

def read_inputs():
    import os
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    with open(file) as f:
        return f.read().strip()

def process(raw):
    return [int(r) if r else 0 for r in raw.split('\n')]

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
