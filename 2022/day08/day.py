import numpy

def part1(inputs):
    size = len(inputs)
    total = 0
    for i in range(size):
        for j in range(size):
            if i == 0 or j == 0 or i == size - 1 or j == size - 1:
                total += 1
                continue

            tree = inputs[i,j]

            # up
            if max(inputs[:i,j]) < tree:
                total += 1
                continue

            # down
            if max(inputs[i+1:,j]) < tree:
                total += 1
                continue

            # left
            if max(inputs[i,:j]) < tree:
                total += 1
                continue

            # right
            if max(inputs[i,j+1:]) < tree:
                total += 1
                continue

    return total

def part2(inputs):
    size = len(inputs)
    biggest = 0
    for i in range(size):
        for j in range(size):
            tree = inputs[i,j]
            prod = 1

            directions = (
                    inputs[:i,j][::-1],
                    inputs[i+1:,j],
                    inputs[i,:j][::-1],
                    inputs[i,j+1:],
            )

            for dr in directions:
                for k, t in enumerate(dr):
                    if t >= tree:
                        prod *= k + 1
                        break
                else:
                    prod *= len(dr)

            biggest = max(biggest, prod)

    return biggest

def read_inputs():
    import os
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    with open(file) as f:
        return f.read().strip()

def process(raw):
    return numpy.array([[int(d) for d in r] for r in raw.split()])

if __name__ == '__main__':
    read = read_inputs()
    print(part1(process(read)))
    print(part2(process(read)))
