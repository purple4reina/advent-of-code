def part1(inputs):
    total, cnt, val, vals = 0, 1, 1, [1]
    indexes = (20, 60, 100, 140, 180, 220)
    for cmd in inputs:
        if cmd == 'noop':
            cnt += 1
            vals.append(val)
            if cnt in indexes:
                total += cnt * val
        else:
            cnt += 1
            vals.append(val)
            if cnt in indexes:
                total += cnt * val
            cnt += 1
            val += int(cmd[5:])
            vals.append(val)
            if cnt in indexes:
                total += cnt * val
    return total

def part2(inputs):
    pass

def read_inputs():
    import os
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    with open(file) as f:
        return f.read().strip()

def process(raw):
    return raw.split('\n')

if __name__ == '__main__':
    read = read_inputs()
    print(part1(process(read)))
    print(part2(process(read)))
