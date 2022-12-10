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

    class State(object):
        def __init__(self):
            self.cycle = self.value = self.sprite = 1
            self.crt = [1] + [0] * 241
        def noop(self):
            self.sprite = self.cycle % 40
            self.crt[self.cycle] = abs(self.sprite - self.value) < 2
            self.cycle += 1
        def addx(self, val):
            self.noop()
            self.value += val
            self.noop()
        @property
        def screen(self):
            crt = []
            for i in range(0, 40*6, 40):
                crt.append(''.join(
                    ('#' if b else '.' for b in self.crt[i:i+40])))
            return '\n'.join(crt)

    state = State()
    for cmd in inputs:
        if cmd == 'noop':
            state.noop()
        else:
            state.addx(int(cmd[5:]))
    return state.screen

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
