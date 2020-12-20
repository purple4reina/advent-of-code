def rev(n, pos=10):
    rev = 0
    while n:
        pos -= 1
        if n & 1:
            rev |= (1 << pos)
        n >>= 1
    return rev


def parse(f):
    tiles = []
    tile = []
    num = None
    for line in f:
        if not line:
            tiles.append((int(num),) + build(tile))
            tile.clear()
            num = None
            continue
        elif num is None:
            num = line.split(' ')[1].rstrip(':')
        else:
            tile.append(line)
    tiles.append((int(num),) + build(tile))
    return tiles


def build(tile):
    b1 = int(''.join(('1' if c == '#' else '0' for c in tile[0])), 2)
    b2 = int(''.join(('1' if t[-1] == '#' else '0' for t in tile)), 2)
    b3 = int(''.join(('1' if c == '#' else '0' for c in tile[-1][::-1])), 2)
    b4 = int(''.join(('1' if t[0] == '#' else '0' for t in tile[::-1])), 2)
    return (b1, b2, b3, b4)


def orientations(t):
    yield (t[0], t[1], t[2], t[3], t[4])
    yield (t[0], t[2], t[3], t[4], t[1])
    yield (t[0], t[3], t[4], t[1], t[2])
    yield (t[0], t[4], t[1], t[2], t[3])

    t = (t[0], rev(t[3]), rev(t[2]), rev(t[1]), rev(t[4]))

    yield (t[0], t[1], t[2], t[3], t[4])
    yield (t[0], t[2], t[3], t[4], t[1])
    yield (t[0], t[3], t[4], t[1], t[2])
    yield (t[0], t[4], t[1], t[2], t[3])


def solve(f):
    tiles = parse(f)
    tot = len(tiles)
    root = int(tot ** 0.5)

    def fits(state, pos, orient):
        row, col = divmod(pos, root)
        if row:
            if orient[1] != rev(state[pos-root][3]):
                return False
        if col:
            if orient[4] != rev(state[pos-1][2]):
                return False
        return True

    def answer(s):
        return s[0][0] * s[root-1][0] * s[-1][0] * s[tot-root][0]

    def search(state, pos):
        for tile in tiles:
            if tile[0] in (s[0] for s in state[:pos]):
                continue
            for orient in orientations(tile):
                if not fits(state, pos, orient):
                    continue
                state[pos] = orient
                if pos == tot - 1:
                    return answer(state)
                ans = search(state, pos + 1)
                if ans:
                    return ans

    return search([None] * tot, 0)


if __name__ == '__main__':
    with open('input.txt') as f:
        print(solve([l.strip() for l in f]))
