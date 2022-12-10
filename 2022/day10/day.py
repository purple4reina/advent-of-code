def part1(inputs):

    class State(object):
        indexes = (20, 60, 100, 140, 180, 220)
        def __init__(self):
            self.count = 1
            self.total = 0
            self.value = 1
            self.values = [1]
        def incr_cnt(self):
            self.count += 1
            self.values.append(self.value)
            if self.count in self.indexes:
                self.total += self.count * self.value
        def incr_val_cnt(self, val):
            self.value += val
            self.incr_cnt()

    state = State()
    for cmd in inputs:
        if cmd == 'noop':
            state.incr_cnt()
        else:
            state.incr_cnt()
            state.incr_val_cnt(int(cmd[5:]))
    return state.total

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
