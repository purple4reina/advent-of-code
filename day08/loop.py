def parse_machine(f):
    m = []
    for line in f:
        cmd, amt = line.split(' ')
        amt = int(amt)
        m.append((cmd, amt))
    return m


def solve(f):
    machine = parse_machine(f)

    for i in range(len(machine)):
        new_machine = machine.copy()
        if new_machine[i][0] == 'jmp':
            new_machine[i] = ('nop', new_machine[i][1])
        elif new_machine[i][0] == 'nop':
            new_machine[i] = ('jmp', new_machine[i][1])
        acc, looped = run(new_machine)
        if not looped:
            break

    return acc


def run(machine):
    accumulator = 0
    index = 0
    states = {}
    looped = False
    while True:
        states[index] = True
        try:
            cmd, amt = machine[index]
        except IndexError:
            break
        if cmd == 'acc':
            accumulator += amt
            index += 1
        elif cmd == 'jmp':
            index += amt
        else:
            index += 1
        if states.get(index):
            looped = True
            break

    return accumulator, looped


if __name__ == '__main__':
    with open('input.txt') as f:
        print(solve(f))
