def part1(points, _y=10):
    world = {}
    for sx, sy, bx, by in points:
        dist = abs(sx - bx) + abs(sy - by)
        for x in range(-dist, dist + 1):
            for y in range(-dist, dist + 1):
                if abs(x) + abs(y) > dist:
                    continue
                world[(sx + x, sy + y)] = True

    total = 0
    for x, y in world:
        if y == _y:
            total += 1
    return total - 1

def part2(inputs):
    pass

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
    print(part1(process(read), y=2000000))
    print(part2(process(read)))
