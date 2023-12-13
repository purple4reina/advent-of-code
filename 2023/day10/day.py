def part1(inputs):
    rows, columns = len(inputs), len(inputs[0])
    for y in range(rows):
        for x in range(columns):
            if inputs[y][x] == 'S':
                break
        else:
            continue
        break

    prevx, prevy = x, y
    while True:
        if y - 1 > 0:
            if inputs[y-1][x] in ('7', '|', 'F'):
                y -= 1
                break
        if y + 1 <= rows:
            if inputs[y+1][x] in ('J', '|', 'L'):
                y += 1
                break
        if x - 1 > 0:
            if inputs[y][x-1] in ('F', '-', 'L'):
                x -= 1
                break
        if x + 1 <= columns:
            if inputs[y][x+1] in ('J', '-', '7'):
                x += 1
                break
    nextx, nexty = x, y

    dist = 0
    while dist < rows * columns:
        dist += 1

        char = inputs[y][x]
        if char == 'S':
            break
        elif x == prevx - 1:
            if char == 'F':
                nexty += 1
            elif char == '-':
                nextx -= 1
            elif char == 'L':
                nexty -= 1
        elif x == prevx + 1:
            if char == 'J':
                nexty -= 1
            elif char == '-':
                nextx += 1
            elif char == '7':
                nexty += 1
        elif y == prevy - 1:
            if char == '7':
                nextx -= 1
            elif char == '|':
                nexty -= 1
            elif char == 'F':
                nextx += 1
        elif y == prevy + 1:
            if char == 'L':
                nextx += 1
            elif char == '|':
                nexty += 1
            elif char == 'J':
                nextx -= 1

        prevx, prevy, x, y = x, y, nextx, nexty

    return dist // 2

def part2(inputs):
    pass

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    return list(raw.split('\n'))

if __name__ == '__main__':
    read = read_inputs()
    print(part1(process(read)))
    print(part2(process(read)))
