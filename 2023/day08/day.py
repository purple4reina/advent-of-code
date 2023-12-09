import math

def part1(inputs):
    turns, nodes = inputs
    loc, count = 'AAA', 0
    while loc != 'ZZZ':
        turn = turns[count % len(turns)]
        left, right = nodes[loc]
        loc = left if turn == 'L' else right
        count += 1
    return count

def part2(inputs):
    def lcm(a, b):
        if a < 0 or b < 0:
            raise ValueError("Inputs must be non-negative")
        if a == 0 or b == 0:
            return 0
        return (a * b) // math.gcd(a, b)

    turns, nodes = inputs
    locs = [node for node in nodes if node[-1] == 'A']
    counts = 1
    for loc in locs:
        count = 0
        while not loc.endswith('Z'):
            turn = turns[count % len(turns)]
            left, right = nodes[loc]
            loc = left if turn == 'L' else right
            count += 1
        counts = lcm(counts, count)
    return counts

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    turns, raw = raw.split('\n\n')
    nodes = {}
    for row in raw.split('\n'):
        start, ends = row.split(' = ')
        left, right = ends.strip('()').split(', ')
        nodes[start] = (left, right)
    return turns, nodes

if __name__ == '__main__':
    read = read_inputs()
    print(part1(process(read)))
    print(part2(process(read)))
