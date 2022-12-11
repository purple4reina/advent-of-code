def part1(monkeys, rounds=20):
    for _ in range(rounds):
        for monkey in monkeys:
            for next_monkey, item in monkey.run():
                monkeys[next_monkey].items.append(item)
    one, two = sorted([m.inspected for m in monkeys])[-2:]
    return one * two

def part2(monkeys):
    for m in monkeys:
        m.div = 1
    return part1(monkeys, rounds=10000)

class Monkey(object):

    def __init__(self, index, div=3):
        self.index = index
        self.inspected = 0
        self.div = div

    def test(self, item):
        if self.condition(item):
            return self.true
        return self.false

    def run(self):
        while self.items:
            self.inspected += 1
            item = self.items.pop(0)
            item = self.operation(item)
            item //= self.div
            yield self.test(item), item

def read_inputs():
    import os
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    with open(file) as f:
        return f.read().strip()

def process(raw):
    def make_operation(inputs):
        _, op, num = inputs.split()
        if op == '+':
            if num == 'old':
                return lambda a: a + a
            num = int(num)
            return lambda a: a + num
        else:
            if num == 'old':
                return lambda a: a**2
            num = int(num)
            return lambda a: a * num

    def make_test(den):
        def test(num):
            return num % den == 0
        return test

    monkeys = []
    for row in raw.split('\n'):
        row = row.strip()
        if row.startswith('Monkey'):
            monkey = Monkey(int(row.split()[1][:-1]))
        elif row.startswith('Starting items'):
            monkey.items = [int(v) for v in row.split(': ')[1].split(', ')]
        elif row.startswith('Operation'):
            monkey.operation = make_operation(row.split(' = ')[1])
        elif row.startswith('Test'):
            monkey.condition = make_test(int(row.split(' by ')[1]))
        elif row.startswith('If true'):
            monkey.true = int(row[-1])
        elif row.startswith('If false'):
            monkey.false = int(row[-1])
        else:
            monkeys.append(monkey)
    monkeys.append(monkey)

    return monkeys

if __name__ == '__main__':
    read = read_inputs()
    print(part1(process(read)))
    print(part2(process(read)))
