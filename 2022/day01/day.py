def part1(inputs):
    top_e = 0
    for elf in inputs:
        top_e = max(sum(elf), top_e)
    return top_e

def part2(inputs):
    vals = []
    for elf in inputs:
        vals.append(sum(elf))
    return sum(sorted(vals)[-3:])

def read_inputs():
    import os
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    with open(file) as f:
        return f.read().strip()

def process(raw):
    return [[int(r) for r in c.split()] for c in raw.split('\n\n')]

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
