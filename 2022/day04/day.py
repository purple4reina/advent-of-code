def part1(inputs):
    count = 0
    for amin, amax, bmin, bmax in inputs:
        if (amin <= bmin) and (amax >= bmax):
            count += 1
        elif (bmin <= amin) and (bmax >= amax):
            count += 1
    return count

def part2(inputs):
    count = 0
    for amin, amax, bmin, bmax in inputs:
        # if any number is between the other two
        if (amin >= bmin) and (amin <= bmax):
            count += 1
        elif (amax >= bmin) and (amax <= bmax):
            count += 1
        elif (bmin >= amin) and (bmin <= amax):
            count += 1
        elif (bmax >= amin) and (bmax <= amax):
            count += 1
    return count

def read_inputs():
    import os
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    with open(file) as f:
        return f.read().strip()

def process(raw):
    l = []
    for pair in raw.split('\n'):
        one, two = pair.split(',')
        a1, a2 = one.split('-')
        b1, b2 = two.split('-')
        l.append((int(a1), int(a2), int(b1), int(b2)))
    return l

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
