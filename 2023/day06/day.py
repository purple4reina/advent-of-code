def part1(inputs):
    total = 1
    for time, dist in inputs:
        count = 0
        for t in range(time + 1):
            d = t * (time - t)
            count += t * (time - t) > dist
        total *= count
    return total

def part2(inputs):
    time = dist = ''
    for t, d in inputs:
        time += str(t)
        dist += str(d)
    time, dist = int(time), int(dist)

    count = 0
    for t in range(time + 1):
        d = t * (time - t)
        count += t * (time - t) > dist

    return count

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    time, dist = raw.split('\n')
    times = [int(t.strip()) for t in time.split(': ')[1].split()]
    dists = [int(d.strip()) for d in dist.split(': ')[1].split()]
    return list(zip(times, dists))

if __name__ == '__main__':
    read = read_inputs()
    print(part1(process(read)))
    print(part2(process(read)))
