def correct_order(left, right):
    while left and right:
        l, r = left.pop(0), right.pop(0)
        lint, rint = isinstance(l, int), isinstance(r, int)

        if lint and rint:
            if l == r:
                continue
            return l < r
        elif lint:
            res = correct_order([l], r)
            if res is None:
                continue
            return res
        elif rint:
            res = correct_order(l, [r])
            if res is None:
                continue
            return res
        else:
            res = correct_order(l, r)
            if res is None:
                continue
            return res

    lleft, lright = len(left), len(right)
    if lleft == lright:
        return None
    return lleft < lright

def correct_indexes(inputs):
    indexes = []
    for i, (left, right) in enumerate(inputs):
        if correct_order(left, right):
            indexes.append(i + 1)
    return indexes

def part1(inputs):
    return sum(correct_indexes(inputs))

def part2(inputs):
    pass

def read_inputs():
    import os
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    with open(file) as f:
        return f.read().strip()

def process(raw):
    packets = []
    raw = raw.split('\n')
    for i in range(0, len(raw), 3):
        packets.append((
            eval(raw[i].strip()),
            eval(raw[i+1].strip()),
        ))
    return packets

if __name__ == '__main__':
    read = read_inputs()
    print(part1(process(read)))
    print(part2(process(read)))
