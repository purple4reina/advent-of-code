import numpy as np

def part1(universe):
    rows, columns = universe.shape
    expanded = np.array(universe)
    for row in reversed(range(rows)):
        if not np.sum(universe[row]):
            expanded = np.insert(expanded, row, 0, axis=0)
    for column in reversed(range(columns)):
        if not np.sum(universe[:,column]):
            expanded = np.insert(expanded, column, 0, axis=1)

    points = []
    exrows, excolumns = expanded.shape
    for y in range(exrows):
        for x in range(excolumns):
            if expanded[y,x] == 1:
                points.append((x, y))

    dist = 0
    pntcnt = len(points)
    for i in range(pntcnt):
        point1 = points[i]
        for j in range(i + 1, pntcnt):
            point2 = points[j]
            dist += abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    return dist

def part2(universe):
    rows, columns = universe.shape
    expanded = np.array(universe)
    for row in reversed(range(rows)):
        if not np.sum(universe[row]):
            expanded = np.insert(expanded, row, np.zeros((1000000, 1)), axis=0)
    for column in reversed(range(columns)):
        if not np.sum(universe[:,column]):
            expanded = np.insert(expanded, column, np.zeros((1000000, 1)), axis=1)

    points = []
    exrows, excolumns = expanded.shape
    for y in range(exrows):
        for x in range(excolumns):
            if expanded[y,x] == 1:
                points.append((x, y))

    dist = 0
    pntcnt = len(points)
    for i in range(pntcnt):
        point1 = points[i]
        for j in range(i + 1, pntcnt):
            point2 = points[j]
            dist += abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    return dist

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    array = []
    for row in raw.split('\n'):
        rowarr = []
        for char in row:
            rowarr.append(1 if char == '#' else 0)
        array.append(rowarr)
    return np.array(array)

if __name__ == '__main__':
    read = read_inputs()
    print(part1(process(read)))
    print(part2(process(read)))
