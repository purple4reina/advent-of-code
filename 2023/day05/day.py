def part1(inputs):
    starts, maps = inputs
    for this_maps in maps:
        next_starts = []
        for start in starts:
            for i, j, k in this_maps:
                if start >= j and start < j + k:
                    start = i - j + start
                    break
            next_starts.append(start)
        starts = next_starts
    return min(starts)

def part2(inputs):
    start_ranges, maps = inputs

    starts = []
    while start_ranges:
        start, num = start_ranges.pop(0), start_ranges.pop(0)
        for s in range(start, start + num + 1):
            starts.append(s)

    for this_maps in maps:
        next_starts = []
        for start in starts:
            for i, j, k in this_maps:
                if start >= j and start < j + k:
                    start = i - j + start
                    break
            next_starts.append(start)
        starts = next_starts
    return min(starts)

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    raw = list(raw.split('\n'))
    inputs = raw.pop(0)
    starts = list(map(int, inputs.split(': ')[1].split()))
    raw.pop(0)

    maps = []
    while raw:
        this_map = []
        raw.pop(0)
        line = raw.pop(0)
        while line:
            this_map.append(list(map(int, line.split())))
            if not raw:
                break
            line = raw.pop(0)
        maps.append(this_map)

    return starts, maps

if __name__ == '__main__':
    read = read_inputs()
    print(part1(process(read)))
    print(part2(process(read)))
