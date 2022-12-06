def part_factory(length):
    def part(inputs):
        for i in range(length-1, len(inputs)):
            msg = inputs[i-length+1:i+1]
            if len(set(msg)) == length:
                return i + 1
    return part

part1 = part_factory(4)
part2 = part_factory(14)

def read_inputs():
    import os
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    with open(file) as f:
        return f.read().strip()

def process(raw):
    return raw

if __name__ == '__main__':
    read = read_inputs()
    print(part1(process(read)))
    print(part2(process(read)))
