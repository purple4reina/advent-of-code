def part1(inputs):
    total = 0
    for seq in inputs:
        t = total
        while any(seq):
            total += seq[-1]
            seq = [seq[i] - seq[i-1] for i in range(1, len(seq))]
    return total

def part2(inputs):
    total = 0
    for seq in inputs:
        mult = 1
        while any(seq):
            total += seq[0] * mult
            seq = [seq[i] - seq[i-1] for i in range(1, len(seq))]
            mult *= -1
    return total

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
