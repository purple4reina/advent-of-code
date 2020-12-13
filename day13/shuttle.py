def solve(inp):
    buses, last = {}, 0
    for i, bus in enumerate(inp[1].split(',')):
        try:
            bus = int(bus)
        except ValueError:
            continue
        buses[bus] = i
        last = i

    stop = 1
    for b in buses:
        stop *= b

    delta = max(buses)
    t = delta + last - buses[delta]
    while True:
        for bus, i in buses.items():
            if (t - last + i) % bus != 0:
                break
        else:
            return t - last
        t += delta

        assert t < stop


if __name__ == '__main__':
    with open('input.txt') as f:
        print(solve(tuple(f)))
