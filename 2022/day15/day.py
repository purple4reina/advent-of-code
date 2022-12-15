def part1(points, _y=10):
    world = {}
    for sx, sy, bx, by in points:
        dist = abs(sx - bx) + abs(sy - by)

        if sy > _y:
            if sy - dist > _y:
                continue
        else:
            if sy + dist < _y:
                continue

        for y in range(dist + 1):
            if sy + y != _y and sy - y != _y:
                continue
            for x in range(dist - y + 1):
                world[(sx + x, sy + y)] = True
                world[(sx + x, sy - y)] = True
                world[(sx - x, sy + y)] = True
                world[(sx - x, sy - y)] = True

    total = 0
    for x, y in world:
        if y == _y:
            total += 1
    return total - 1

def part2(points, most=20):

    def tuning(x, y):
        return 4000000 * x + y

    world = {}
    for sx, sy, bx, by in points:
        dist = abs(sx - bx) + abs(sy - by)

#        if sx < 0:
#            if sx + dist < 0:
#                continue
#        elif sx > most:
#            if sx - dist > most:
#                continue
#        elif sy < 0:
#            if sy + dist < 0:
#                continue
#        elif sy > most:
#            if sy - dist > most:
#                continue

        for y in range(dist + 1):
            #            if sy + y < 0 and sy + y > most and sy - y < 0 and sy - y > most:
            #                continue
            for x in range(dist - y + 1):
                #                if sx + x > most:
                #                    break
                world[(sx + x, sy + y)] = True
                world[(sx + x, sy - y)] = True
                world[(sx - x, sy + y)] = True
                world[(sx - x, sy - y)] = True

    #import numpy as np
    #w = np.array([[x, y] for x, y in world.keys()])
    #import matplotlib.pyplot as plot
    #plot.plot(w[:,0], w[:,1], 'ro')
    #plot.xlim([0, most])
    #plot.ylim([0, most])
    #plot.show()

    xs = [0] * (most + 1)
    ys = [0] * (most + 1)
    for x, y in world:
        if x >= 0 and x <= most and y >= 0 and y <= most:
            xs[x] += 1
            ys[y] += 1

    print('xs,ys: ', xs,ys)
    lx = ly = float('inf')
    ix = iy = None
    for i, x in enumerate(xs):
        if x < lx:
            lx = x
            ix = i
    for i, y in enumerate(ys):
        if y < ly:
            ly = y
            iy = i
    return tuning(ix, iy)

def read_inputs():
    import os
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    with open(file) as f:
        return f.read().strip()

def process(raw):
    import re
    points = []
    row_re = re.compile(
            r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')
    for row in raw.split('\n'):
        m = row_re.match(row)
        point = tuple(map(int, m.groups()))
        points.append(point)
    return points

if __name__ == '__main__':
    read = read_inputs()
    print(part1(process(read), _y=2000000))
    print(part2(process(read), most=4000000))
