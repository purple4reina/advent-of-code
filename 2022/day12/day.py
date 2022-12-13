def part1(inputs):
    hmap, (begy, begx), (endy, endx) = inputs
    height, width = len(hmap), len(hmap[0])
    vmap = [[None for _ in range(width)] for _ in range(height)]

    # start with S
    # for each location in the set
    #   for each unvisited neighbor of this location
    #       if this neighbor is the end, we're done
    #       set the value (+1 from the prev value) in vmap

    def unvisited_neighbors(locx, locy):
        for newx, newy in [
                (locx-1, locy), (locx+1, locy), (locx, locy-1), (locx, locy+1)]:
            if newx < 0 or newx >= width or newy < 0 or newy >= height:
                continue
            if vmap[newy][newx] is not None:
                continue
            if hmap[newy][newx] - hmap[locy][locx] > 1:
                continue
            yield newx, newy

    last_visited, new_visited, step = [(begx, begy)], [], 1
    while last_visited:
        for locx, locy in last_visited:
            for newx, newy in unvisited_neighbors(locx, locy):
                if newx == endx and newy == endy:
                    return step
                vmap[newy][newx] = step
                new_visited.append((newx, newy))
        last_visited, new_visited, step = new_visited, [], step + 1

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
