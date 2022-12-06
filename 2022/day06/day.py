def part1(inputs):
    _1 = _2 = _3 = _4 = None
    for i in range(len(inputs)):
        _1, _2, _3, _4 = _2, _3, _4, inputs[i]
        if i < 4:
            continue
        if len(set((_1, _2, _3, _4))) == 4:
            return i + 1

def part2(inputs):
    _1 = _2 = _3 = _4 = _5 = _6 = _7 = _8 = _9 = _10 = _11 = _12 = _13 = _14 = None
    for i in range(len(inputs)):
        _1, _2, _3, _4, _5, _6, _7, _8, _9, _10, _11, _12, _13, _14 = (
            _2, _3, _4, _5, _6, _7, _8, _9, _10, _11, _12, _13, _14, inputs[i])
        if i < 14:
            continue
        if len(set((_1, _2, _3, _4, _5, _6, _7, _8, _9, _10, _11, _12, _13,
                    _14))) == 14:
            return i + 1

def read_inputs():
    import os
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    with open(file) as f:
        return f.read().strip()

def process(raw):
    return raw

if __name__ == '__main__':
    read = read_inputs()
    print(part1(process(read)))
    print(part2(process(read)))
