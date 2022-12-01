def parse(n):
    cube = {}
    for i, r in enumerate(n):
        for j, p in enumerate(r):
            cube[(i, j, 0, 0)] = (p == '#')
    return cube


def active(x_val, y_val, z_val, w_val, cube):
    act = 0
    for x in range(x_val - 1, x_val + 2):
        for y in range(y_val - 1, y_val + 2):
            for z in range(z_val - 1, z_val + 2):
                for w in range(w_val - 1, w_val + 2):
                    if x == x_val and y == y_val and z == z_val and w == w_val:
                        continue
                    act += (cube.get((x, y, z, w)) is True)
    return act


def cycle(c):
    cube = {}
    x_min, y_min, z_min, w_min = min(c)
    x_max, y_max, z_max, w_max = max(c)
    for x in range(x_min - 1, x_max + 2):
        for y in range(y_min - 1, y_max + 2):
            for z in range(z_min - 1, z_max + 2):
                for w in range(w_min - 1, w_max + 2):
                    act = active(x, y, z, w, c)
                    if c.get((x, y, z, w)):
                        cube[(x, y, z, w)] = (act == 2 or act == 3)
                    else:
                        cube[(x, y, z, w)] = (act == 3)
    return cube


def solve(n):
    xy = len(n)
    cube = parse(n)
    for _ in range(6):
        cube = cycle(cube)
    return sum(cube.values())


if __name__ == '__main__':
    with open('input.txt') as f:
        print(solve([l.strip() for l in f]))
