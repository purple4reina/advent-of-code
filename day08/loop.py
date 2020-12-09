def parse_machine(f):
    m = []
    for line in f:
        cmd, amt = line.split(' ')
        amt = int(amt)
        m.append((cmd, amt))
    return m


def solve(f):
    machine = parse_machine(f)
    states = {}

    accumulator = 0
    index = 0
    while True:
        states[index] = True
        cmd, amt = machine[index]
        if cmd == 'acc':
            accumulator += amt
            index += 1
        elif cmd == 'jmp':
            index += amt
        else:
            index += 1
        if states.get(index):
            break

    return accumulator


if __name__ == '__main__':
    with open('input.txt') as f:
        print(solve(f))
