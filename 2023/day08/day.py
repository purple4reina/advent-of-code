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
    pass

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
