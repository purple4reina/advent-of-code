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
    total, total_rows, total_columns = 0, len(inputs), len(inputs[0])
    for row in range(total_rows):
        for col in range(total_columns):
            if inputs[row][col] != '*':
                continue
            parts_found = 0
            for i in range(row-1, row+2):
                if i < 0 or i >= total_rows:
                    continue
                digit_found = False
                for j in range(col-1, col+2):
                    if j < 0 or j >= total_columns:
                        continue
                    if inputs[i][j] in _digits:
                        if not digit_found:
                            parts_found += 1
                        digit_found = True
                    else:
                        digit_found = False
            if parts_found < 2:
                continue
            gear_ratio = 1
            for i in range(row-1, row+2):
                if i < 0 or i >= total_rows:
                    continue
                digit_found = False
                for j in range(col-1, col+2):
                    if j < 0 or j >= total_columns:
                        continue
                    if not digit_found and inputs[i][j] in _digits:
                        # determine part number
                        part_start = part_end = j
                        while part_start > 0:
                            if inputs[i][part_start-1] not in _digits:
                                break
                            part_start -= 1
                        while part_end < total_columns - 1:
                            if inputs[i][part_end+1] not in _digits:
                                break
                            part_end += 1
                        gear_ratio *= int(''.join(inputs[i][part_start:part_end+1]))
                    digit_found = inputs[i][j] in _digits
            total += gear_ratio
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
