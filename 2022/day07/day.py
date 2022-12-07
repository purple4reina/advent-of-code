def size_of_dir(inputs):
    filesys = curdir = {}
    filesys['/'] = filesys

    # construct file system
    for cmd in inputs:
        if cmd.startswith('$ cd'):
            _, c, v = cmd.split()
            if c == 'cd':
                curdir = curdir[v]
        elif not cmd.startswith('$'):
            t, n = cmd.split()
            curdir[n] = {'/': filesys, '..': curdir} if t == 'dir' else int(t)

    # find directories <= 100000
    totals = []
    def size_of_dir(this_name, this_val):
        if isinstance(this_val, int):
            return this_val
        total = 0
        for next_name, next_val in this_val.items():
            if next_name == '..' or next_name == '/':
                continue
            total += size_of_dir(next_name, next_val)
        totals.append(total)
        return total

    return size_of_dir('/', filesys), totals

def part1(inputs):
    _, totals = size_of_dir(inputs)
    return sum(t for t in totals if t <= 100000)

def part2(inputs):
    total_size, totals = size_of_dir(inputs)
    must_free = total_size - 40000000
    return min(t for t in totals if t > must_free)

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
