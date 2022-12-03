_vals = {
        l: i + 1 for i, l in enumerate(
            'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
}

def part1(inputs):
    total = 0
    for sack in inputs:
        size = len(sack) // 2
        pouch_1 = set(sack[:size])
        pouch_2 = set(sack[size:])
        for item in pouch_1 & pouch_2:
            total += _vals[item]
    return total

def part2(inputs):
    total = 0
    while inputs:
        elf_1 = set(inputs.pop())
        elf_2 = set(inputs.pop())
        elf_3 = set(inputs.pop())
        for item in elf_1 & elf_2 & elf_3:
            total += _vals[item]
    return total

def read_inputs():
    import os
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    with open(file) as f:
        return f.read().strip()

def process(raw):
    return raw.split('\n')

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
