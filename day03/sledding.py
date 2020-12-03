def main(f):
    total = 1
    total *= traverse(1, 1, f)
    total *= traverse(3, 1, f)
    total *= traverse(5, 1, f)
    total *= traverse(7, 1, f)
    total *= traverse(1, 2, f)
    return total


def traverse(right, down, f):
    i = 0
    trees = 0
    d = 0
    for row in f:
        row = row.strip()
        if row[i] == '#' and not d:
            trees += 1
        if not d:
            i = (i + right) % len(row)
        d = (d + 1) % down
    return trees


if __name__ == '__main__':
    with open('input.txt') as f:
        print(main(list(f)))
