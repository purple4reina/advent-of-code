def part1(inputs):
    yard, moves = inputs
    for num, frm, to in moves:
        for _ in range(num):
            crate = yard[frm-1].pop()
            yard[to-1].append(crate)
    return ''.join(s[-1] for s in yard)

def part2(inputs):
    yard, moves = inputs
    for y in yard:
        print(y)
    for num, frm, to in moves:
        frm, to = frm - 1, to - 1
        print('num,frm,to: ', num,frm,to)
        crates = yard[frm][-num:]
        print('crates: ', crates)
        yard[frm][-num:] = []
        yard[to].extend(crates)
        for y in yard:
            print(y)
    return ''.join(s[-1] for s in yard)

def read_inputs():
    import os
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    with open(file) as f:
        return f.read()

def process(raw):
    stacks, procedures = raw.split('\n\n')
    print('stacks: ', stacks)
    print('procedures: ', procedures)

    # crates
    cols = int(stacks.split('\n')[-1].split()[-1])
    yard = [[] for _ in range(cols)]
    for row in stacks.split('\n')[:-1]:
        if not row:
            continue
        for c in range(cols):
            i = c * 4 + 1
            if len(row) <= i:
                break
            val = row[i]
            if val != ' ':
                yard[c].insert(0, val)

    # moves
    moves = []
    for proc in procedures.split('\n'):
        if not proc:
            continue
        _, move, _, frm, _, to = proc.split(' ')
        moves.append((int(move), int(frm), int(to)))

    return yard, moves

if __name__ == '__main__':
    inputs = process(read_inputs())
    #print(part1(inputs))
    print(part2(inputs))
