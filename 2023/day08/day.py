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
    turns, nodes = inputs
    locs = [node for node in nodes if node[-1] == 'A']
    count = 0
    while any(l[-1] != 'Z' for l in locs):
        if count % 1e6 == 0: print('count: ', count)
        turn = turns[count % len(turns)]
        new_locs = []
        for loc in locs:
            left, right = nodes[loc]
            new_locs.append(left if turn == 'L' else right)
        count += 1
        locs = new_locs
    return count

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
