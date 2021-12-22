import numpy as np

def part1(steps):
    reactor = np.zeros((101, 101, 101), dtype=int)
    for action, regions in steps:
        section = []
        for axis, (start, end) in enumerate(regions):
            start, end = start + 50, end + 50 + 1
            section.append(slice(start, end))
        reactor[tuple(section)] = action
    return reactor.sum()

def part2(steps):
    total, prev_steps, new_prev_steps = 0, [], []
    for step, (action, ranges) in enumerate(steps):
        prev_steps, new_prev_steps = new_prev_steps, []
        (xs, xe), (ys, ye), (zs, ze) = ranges
        total += (xe - xs + 1) * (ye - ys + 1) * (ze - zs + 1) * action
        if action:
            new_prev_steps.append((-1, ranges))
        for paction, pranges in prev_steps:
            new_prev_steps.append((paction, pranges))
            (pxs, pxe), (pys, pye), (pzs, pze) = pranges
            mxe, mxs = min(xe, pxe), max(xs, pxs)
            mye, mys = min(ye, pye), max(ys, pys)
            mze, mzs = min(ze, pze), max(zs, pzs)
            pval = (mxe - mxs + 1) * (mye - mys + 1) * (mze - mzs + 1)
            if pval:
                total += pval * paction
                new_prev_steps.append((-paction,
                    ((mxs, mxe), (mys, mye), (mzs, mze))))
    return total

"""
    on x=1..3,y=1..3,z=1..3
    off x=2..4,y=2..4,z=2..4
    on x=1..5,y=1..5,z=1..5

    on sqr a
      add all           a           27
    off sqr b
      sub inter         -a&b        -8
    on sqr c
      add all           c           125
      sub inter        -a&c         -27
      add inter-inter  a&b&c        8

          +------------+
          | a-ON       |
          |    +-------+------+
          |  0 |       |      |
          |    |   0   | b-OFF|
    +-----+----+--+    |      |
    |     | 19 |8 |    |      |
    |     +----+--+----+      |
    |          |19|     0     |
    |  c-ON    |  |           |
    |          +--+-----------+
    |     79      |
    +-------------+
"""

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    steps = []
    for line in raw.split('\n'):
        step = []
        line = line.strip()
        step.append(int(line.startswith('on')))
        regions = []
        for region in line.split()[1].split(','):
            start, stop = map(int, region.split('=')[1].split('..'))
            regions.append((start, stop))
        step.append(regions)
        steps.append(step)
    return steps

if __name__ == '__main__':
    inputs = process(read_inputs())
    print(part1(inputs))
    print(part2(inputs))
