def get_seat_id(code):
    row_min, row_max = 0, 127
    for fb in code[:-3]:
        if fb == 'F':
            row_max = row_min + (row_max - row_min + 1) // 2 - 1
        else:
            row_min = row_max - (row_max - row_min + 1) // 2 + 1
    row = row_min

    col_min, col_max = 0, 7
    for rl in code[-3:]:
        if rl == 'L':
            col_max = col_min + (col_max - col_min + 1) // 2 - 1
        else:
            col_min = col_max - (col_max - col_min + 1) // 2 + 1
    col = col_min

    return row * 8 + col


def main(f):
    seat = 0
    for line in f:
        seat_id = get_seat_id(line.strip())
        if seat_id > seat:
            seat = seat_id
    return seat


if __name__ == '__main__':
    with open('input.txt') as f:
        print(main(f))
