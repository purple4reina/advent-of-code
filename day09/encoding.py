def solve(f, length=25):

    def valid(num):
        for a in seen:
            for b in seen:
                if a == b:
                    break
                if num == a + b:
                    return True
        return False

    seen = []
    for line in f:
        num = int(line.strip())
        if len(seen) < length:
            seen.append(num)
            continue
        if not valid(num):
            return num
        seen.pop(0)
        seen.append(num)


if __name__ == '__main__':
    with open('input.txt') as f:
        print(solve(f))
