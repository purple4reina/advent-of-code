def solve(inp):
    buses = []
    for i, bus in enumerate(inp[1].split(',')):
        try:
            bus = int(bus)
        except ValueError:
            continue
        buses.append((bus, i))

    delta, t = 1, 0
    while True:
        delta = 1
        for bus, i in buses:
            if (t + i) % bus != 0:
                break
            delta *= bus
        else:
            return t
        t += delta


if __name__ == '__main__':
    with open('input.txt') as f:
        print(solve(tuple(f)))
