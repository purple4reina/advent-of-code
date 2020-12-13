def solve(inp):
    time_now, buses = int(inp[0]), inp[1]

    next_bus, wait_time = 0, float('inf')
    for bus in buses.split(','):
        try:
            bus = int(bus)
        except ValueError:
            continue

        dep = 0
        while dep < time_now:
            dep += bus
        wait = dep - time_now
        if wait < wait_time:
            next_bus = bus
            wait_time = wait

    return next_bus * wait_time


if __name__ == '__main__':
    with open('input.txt') as f:
        print(solve(tuple(f)))
