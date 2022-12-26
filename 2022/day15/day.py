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

    ptdist = []
    for sx, sy, bx, by in points:
        dist = abs(sx - bx) + abs(sy - by)
        ptdist.append((sx, sy, dist))

    world = {}
    for sx, sy, dist in ptdist:
        for y in range(dist + 2):
            x = dist + 1 - y
            world[(sx + x, sy + y)] = True
            world[(sx + x, sy - y)] = True
            world[(sx - x, sy + y)] = True
            world[(sx - x, sy - y)] = True

    for x, y in world:
        if x < 0 or x > most or y < 0 or y > most:
            continue
        for sx, sy, d in ptdist:
            dist = abs(sx - x) + abs(sy - y)
            if dist <= d:
                break
        else:
            return 4000000 * x + y

    assert False, 'you should have found an answer'

def read_inputs():
    import os
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    with open(file) as f:
        return f.read().strip()

def process(raw):
    import re
    points = []
    row_re = re.compile(
            r'\s*Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')
    for row in raw.split('\n'):
        m = row_re.match(row)
        point = tuple(map(int, m.groups()))
        points.append(point)
    return points

if __name__ == '__main__':
    read = read_inputs()
    print(part1(process(read), _y=2000000))
    print(part2(process(read), most=4000000))
