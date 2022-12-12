def part1(inputs):
    hmap, (locy, locx), (endy, endx) = inputs
    height, width = len(hmap), len(hmap[0])

    def travel(locx, locy, elev, visited):
        if (locx, locy) in visited:
            return float('inf')
        visited = visited + ((locx, locy),)

        if locx == endx and locy == endy:
            return 0

        shortest = float('inf')
        for x in (-1, 1):
            newx = locx + x
            if newx >= 0 and newx < width:
                new_elev = hmap[locy][newx]
                if new_elev - elev > 1:
                    continue
                val = travel(newx, locy, new_elev, visited) + 1
                shortest = min(shortest, val)

        for y in (-1, 1):
            newy = locy + y
            if newy >= 0 and newy < height:
                new_elev = hmap[newy][locx]
                if new_elev - elev > 1:
                    continue
                val = travel(locx, newy, new_elev, visited) + 1
                shortest = min(shortest, val)

        return shortest

    visited = {}
    return travel(locx, locy, 0, ())

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
