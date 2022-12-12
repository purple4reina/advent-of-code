import sys
sys.setrecursionlimit(45000)

def part1(inputs):
    hmap, (sary, sarx), (endy, endx) = inputs
    height, width = len(hmap), len(hmap[0])

    def travel(locx, locy, visited):
        if (locx, locy) in visited:
            return float('inf')
        visited = visited + ((locx, locy),)

        if locx == sarx and locy == sary:
            return 0

        shortest = float('inf')
        elev = hmap[locy][locx]
        for x in (-1, 1):
            newx = locx + x
            if newx >= 0 and newx < width:
                if hmap[locy][newx] - elev < -1:
                    continue
                val = travel(newx, locy, visited)
                shortest = min(shortest, val + 1)

        for y in (-1, 1):
            newy = locy + y
            if newy >= 0 and newy < height:
                if hmap[newy][locx] - elev < -1:
                    continue
                val = travel(locx, newy, visited)
                shortest = min(shortest, val + 1)

        return shortest

    return travel(endx, endy, ())

def part2(inputs):
    pass

def read_inputs():
    import os
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    with open(file) as f:
        return f.read().strip()

alpha_map = dict((l, i) for i, l in enumerate('abcdefghijklmnopqrstuvwxyz'))
alpha_map['S'] = 0
alpha_map['E'] = 25

def process(raw):
    hmap = [[alpha_map[l] for l in row] for row in raw.split('\n')]

    width = len(hmap[0])
    vals = raw.replace('\n', '')

    start = vals.index('S')
    end = vals.index('E')

    return hmap, divmod(start, width), divmod(end, width)

if __name__ == '__main__':
    read = read_inputs()
    print(part1(process(read)))
    print(part2(process(read)))
