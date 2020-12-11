def cache(fn):
    _cache = {}
    def wrap(*args):
        if args in _cache:
            return _cache[args]
        ret = fn(*args)
        _cache[args] = ret
        return ret
    return wrap


def solve(seating):
    rows = len(seating)
    cols = len(seating[0])

    @cache
    def viewables(row, col):
        views = []
        transforms = (
            (-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),          ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1))

        for row_d, col_d in transforms:
            r, c = row + row_d, col + col_d
            while r >= 0 and c >= 0 and r < rows and c < cols:
                if seating[r][c] != '.':
                    views.append((r, c))
                    break
                r += row_d
                c += col_d

        return views

    def update_seating(seating):

        def count_occupied(row, col):
            count = 0
            for r, c in viewables(row, col):
                count += seating[r][c] == '#'
            return count

        new_seating = []
        for r in range(rows):
            row = ''
            for c in range(cols):
                spot = seating[r][c]
                if spot == 'L' and count_occupied(r, c) == 0:
                    row += '#'
                elif spot == '#' and count_occupied(r, c) > 4:
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
