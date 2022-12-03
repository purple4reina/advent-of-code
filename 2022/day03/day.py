_vals = {
        l: i + 1 for i, l in enumerate(
            'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
}

def part1(inputs):
    total = 0
    for sack in inputs:
        one, two = sack[:len(sack)//2], sack[len(sack)//2:]
        o_items, t_items = {}, {}
        for o in one:
            o_items[o] = True
        for t in two:
            if not t_items.get(t) and o_items.get(t):
                total += _vals[t]
                t_items[t] = True
    return total

def part2(inputs):
    total = 0
    while inputs:
        first, second, third = inputs.pop(), inputs.pop(), inputs.pop()

        items = {}
        for item in first:
            items[item] = True

        for sack in (second, third):
            new_items = {}
            for item in sack:
                if items.get(item):
                    new_items[item] = True
            items, new_items = new_items, {}

        for k, _ in items.items():
            total += _vals[k]

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
