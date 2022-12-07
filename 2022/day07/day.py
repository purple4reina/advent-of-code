def part1(inputs):
    filesys = curdir = {}
    filesys['/'] = filesys

    # construct file system
    for cmd in inputs:
        cmds = cmd.split()
        if cmds[0] == '$':
            if cmds[1] == 'cd':  # $ cd name
                curdir = curdir[cmds[2]]
            else:  # $ ls
                pass
        else:
            if cmds[0] == 'dir':  # dir, name
                curdir[cmds[1]] = {
                        '/': filesys,
                        '..': curdir,
                }
            else:  # size, name
                curdir[cmds[1]] = int(cmds[0])

    # find directories <= 100000
    totals = [0]
    def size_of_dir(this_name, this_val):
        if isinstance(this_val, int):
            return this_val
        total = 0
        for next_name, next_val in this_val.items():
            if next_name == '..' or next_name == '/':
                continue
            total += size_of_dir(next_name, next_val)
        if total <= 100000:
            totals[0] += total
        return total

    size_of_dir('/', filesys)
    return totals[0]

def part2(inputs):
    filesys = curdir = {}
    filesys['/'] = filesys

    # construct file system
    for cmd in inputs:
        cmds = cmd.split()
        if cmds[0] == '$':
            if cmds[1] == 'cd':  # $ cd name
                curdir = curdir[cmds[2]]
            else:  # $ ls
                pass
        else:
            if cmds[0] == 'dir':  # dir, name
                curdir[cmds[1]] = {
                        '/': filesys,
                        '..': curdir,
                }
            else:  # size, name
                curdir[cmds[1]] = int(cmds[0])

    # find directories <= 100000
    totals = [float('inf')]
    must_free = 0
    def size_of_dir(this_name, this_val):
        if isinstance(this_val, int):
            return this_val
        total = 0
        for next_name, next_val in this_val.items():
            if next_name == '..' or next_name == '/':
                continue
            total += size_of_dir(next_name, next_val)
        if must_free and total >= must_free:
            totals[0] = min(totals[0], total)
        return total

    total_size = size_of_dir('/', filesys)
    must_free = total_size - 40000000
    size_of_dir('/', filesys)
    return totals[0]

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
