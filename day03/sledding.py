def main(f):
    i = 0
    trees = 0
    for row in f:
        row = row.strip()
        if row[i] == '#':
            trees += 1
        i = (i + 3) % len(row)
    return trees


if __name__ == '__main__':
    with open('input.txt') as f:
        print(main(f))
