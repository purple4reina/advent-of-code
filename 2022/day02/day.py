# A rock
# B paper
# C scissors

# X rock
# Y paper
# Z scissors

def part1(inputs):
    sym = {
            'A': 1, 'B': 2, 'C': 3,
            'X': 1, 'Y': 2, 'Z': 3,
    }
    score = 0
    for you, me in inputs:
        you, me = sym[you], sym[me]
        score += me
        res = (you - me) % 3
        if res == 1:
            score += 6
        elif res == 2:
            score += 3
    return score

# A rock
# B paper
# C scissors

# X lose
# Y draw
# Z win

def part2(inputs):
    score = 0
    for you, me in inputs:
        if you == 'A':
            if me == 'X':
                score += 0 + 3
            if me == 'Y':
                score += 3 + 1
            if me == 'Z':
                score += 6 + 2
        if you =='B':
            if me == 'X':
                score += 0 + 1
            if me == 'Y':
                score += 3 + 2
            if me == 'Z':
                score += 6 + 3
        if you == 'C':
            if me == 'X':
                score += 0 + 2
            if me == 'Y':
                score += 3 + 3
            if me == 'Z':
                score += 6 + 1
    return score

def read_inputs():
    import os
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    with open(file) as f:
        return f.read().strip()

def process(raw):
    inp = []
    for row in raw.split('\n'):
        inp.append(row.split(' '))
    return inp

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
