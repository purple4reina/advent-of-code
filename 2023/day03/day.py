_digits = tuple(map(str, range(10)))

def part1(inputs):
    total = 0
    for row_number, row in enumerate(inputs):
        current_number = is_part_number = 0
        for i in range(len(row)):
            char = row[i]
            if char not in _digits:
                if is_part_number:
                    total += current_number
                current_number = is_part_number = 0
                continue
            digit = int(char)
            current_number *= 10
            current_number += digit
            if is_part_number:
                continue
            for j in range(row_number-1, row_number+2):
                if is_part_number:
                    break
                if j < 0 or j >= len(inputs):
                    continue
                for k in range(i-1, i+2):
                    if k < 0 or k >= len(row):
                        continue
                    symbol = inputs[j][k]
                    if symbol not in _digits and symbol != '.':
                        is_part_number = True
                        break
        if is_part_number:
            total += current_number
    return total

def part2(inputs):
    pass

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
