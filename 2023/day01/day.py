def part1(inputs):
    total = 0
    for line in inputs:
        num = 0
        for char in line:
            try:
                num += 10 * int(char)
                break
            except:
                pass
        for char in line[::-1]:
            try:
                num += int(char)
                break
            except:
                pass
        total += num
    return total

_part2_map = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
}
def part2(inputs):
    total = 0
    for line in inputs:
        first = num = None
        for index in range(len(line)):
            char = line[index]
            try:
                num = int(char)
            except:
                for d in range(3, 6):
                    try:
                        key = line[index:index+d]
                        num = _part2_map[key]
                        break
                    except:
                        pass
            if first is None and num is not None:
                first = num
        print('first*10+num: ', first*10+num)
        total += first * 10 + num
    return total

def read_inputs():
    import os
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    with open(file) as f:
        return f.read().strip()

def process(raw):
    return list(raw.split())

if __name__ == '__main__':
    read = read_inputs()
    print(part1(process(read)))
    print(part2(process(read)))
