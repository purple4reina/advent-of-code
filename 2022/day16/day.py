def part1(system):

    states, new_states = [(0, 'AA', [])], []
    top = 0
    for minute in range(1, 31):
        for total, loc, opened in states:

            rate, valves = system[loc]

            # open
            if loc not in opened:
                new_states.append((total + rate*(30-minute), loc, opened+[loc]))

            # move
            for valve in valves:
                new_states.append((total, valve, opened))

        states, new_states = new_states, []
        states.sort(reverse=True)
        states = states[:len(states)//2+4]

    top = 0
    for total, _, _ in states:
        top = max(top, total)
    return top

#    most = [0]
#    def release(loc, minute, opened):
#        minute += 1
#
#        if minute > 30:
#            return 0
#
#        rate, valves = system[loc]
#
#        # open valve
#        val = 0
#        if loc not in opened:
#            val = max(rate*(30-minute) + release(loc, minute, opened+[loc]), val)
#
#        # move
#        for valve in valves:
#            val = max(release(valve, minute, opened), val)
#
#        if val > most[0]:
#            most[0] = val
#            print('val: ', val)
#        return val
#
#    return release('AA', 0, [])

def part2(inputs):
    pass

def read_inputs():
    import os
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    with open(file) as f:
        return f.read().strip()

def process(raw):
    import re
    system = {}
    row_re = re.compile(
            r'Valve (..) has flow rate=(\d*); tunnels? leads? to valves? (.*)')
    for row in raw.split('\n'):
        m = row_re.match(row)
        loc = m.group(1)
        rate = int(m.group(2))
        valves = list(m.group(3).split(', '))
        system[loc] = (rate, valves)
    return system

if __name__ == '__main__':
    read = read_inputs()
    print(part1(process(read)))
    print(part2(process(read)))
