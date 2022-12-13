import copy
import functools

def correct_order(left, right):
    left, right = copy.deepcopy(left), copy.deepcopy(right)
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

def as_sort_key(fn):
    def wrap(a, b):
        val = fn(a, b)
        if val is True:
            return 1
        if val is False:
            return -1
        return 0
    return wrap

def part1(inputs):
    return sum(correct_indexes(inputs))

def part2(inputs):
    inp = []
    for a, b in inputs:
        inp.append(a)
        inp.append(b)

    divider1 = [[2]]
    divider2 = [[6]]
    inp.append(divider1)
    inp.append(divider2)

    print('--------------------inp--------------------')
    for i in inp:
        print(i)

    sorted_inputs = sorted(
            inp, key=functools.cmp_to_key(as_sort_key(correct_order)),
            reverse=True)
    print('--------------------sorted--------------------')
    for s in sorted_inputs:
        print(s)

    index1 = sorted_inputs.index(divider1) + 1
    index2 = sorted_inputs.index(divider2) + 1
    return index1 * index2

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
