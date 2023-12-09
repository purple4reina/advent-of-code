def part1(inputs):
    total = 0
    for seq in inputs:
        seqs = [seq]
        while sum(seq):
            seq = [seq[i] - seq[i-1] for i in range(1, len(seq))]
            seqs.append(seq)
        num = 0
        for seq in reversed(seqs):
            num += seq[-1]
        total += num
    return total

def part2(inputs):
    pass

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    for row in raw.split('\n'):
        yield list(map(int, row.split()))

if __name__ == '__main__':
    read = read_inputs()
    print(part1(process(read)))
    print(part2(process(read)))
