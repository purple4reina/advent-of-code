def part1(inputs):
    hx = hy = tx = ty = 0
    visited = {(0, 0): True}
    for d, n in inputs:
        for _ in range(n):
            # update head
            if d == 'R':
                hx += 1
            if d == 'L':
                hx -= 1
            if d == 'U':
                hy += 1
            if d == 'D':
                hy -= 1

            # update tail
            x_within_1, y_within_1 = abs(hx - tx) <= 1, abs(hy - ty) <= 1
            same_column, same_row = hx == tx, hy == ty
            if x_within_1 and y_within_1:
                pass
            elif same_column and not y_within_1:
                if hy > ty:
                    ty += 1
                else:
                    ty -= 1
            elif same_row and not x_within_1:
                if hx > tx:
                    tx += 1
                else:
                    tx -= 1
            else:
                if hy > ty:
                    ty += 1
                else:
                    ty -= 1
                if hx > tx:
                    tx += 1
                else:
                    tx -= 1

            visited[(tx, ty)] = True

    return len(visited)

def part2(inputs):
    knots = [(0, 0) for _ in range(10)]
    visited = {(0, 0): True}
    for d, n in inputs:
        for _ in range(n):
            hx, hy = knots[0]
            if d == 'R':
                hx += 2
            if d == 'L':
                hx -= 2
            if d == 'U':
                hy += 2
            if d == 'D':
                hy -= 2

            for i in range(10):
                tx, ty = knots[i]
                x_within_1, y_within_1 = abs(hx - tx) <= 1, abs(hy - ty) <= 1
                same_column, same_row = hx == tx, hy == ty

                if x_within_1 and y_within_1:
                    pass
                elif same_row and not x_within_1:
                    tx += 1 if hx > tx else -1
                elif same_column and not y_within_1:
                    ty += 1 if hy > ty else -1
                else:
                    tx += 1 if hx > tx else -1
                    ty += 1 if hy > ty else -1

                hx, hy = knots[i] = (tx, ty)
            visited[(tx, ty)] = True
    return len(visited)

def read_inputs():
    import os
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    with open(file) as f:
        return f.read().strip()

def process(raw):
    a = []
    for b in raw.split('\n'):
        if not b:
            continue
        x, y = b.split()
        a.append((x, int(y)))
    return a

if __name__ == '__main__':
    read = read_inputs()
    print(part1(process(read)))
    print(part2(process(read)))
