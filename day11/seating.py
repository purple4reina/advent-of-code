def solve(seating):
    rows = len(seating)
    cols = len(seating[0])

    def update_seating(seating):

        def count_occupied(row, col):
            count = 0
            for r in range(max(0, row-1), min(row+2, rows)):
                for c in range(max(0, col-1), min(col+2, cols)):
                    if r == row and c == col:
                        continue
                    count += seating[r][c] == '#'
            return count

        new_seating = []
        for r in range(rows):
            row = ''
            for c in range(cols):
                spot = seating[r][c]
                if spot == 'L' and count_occupied(r, c) == 0:
                    row += '#'
                elif spot == '#' and count_occupied(r, c) > 3:
                    row += 'L'
                else:
                    row += spot
            new_seating.append(row)
        return new_seating

    prev_seating = []
    while prev_seating != seating:
        prev_seating, seating = seating, update_seating(seating)

    return ''.join(seating).count('#')


if __name__ == '__main__':
    with open('input.txt') as f:
        print(solve(list(line.strip() for line in f)))
