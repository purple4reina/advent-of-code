def solve(f):
    nums = []
    for line in f:
        nums.append(int(line))
    nums.sort()

    prev = ones = 0
    threes = 1
    for num in nums:
        diff = num - prev
        if diff == 1:
            ones += 1
        elif diff == 3:
            threes += 1
        prev = num

    return ones * threes


if __name__ == '__main__':
    with open('input.txt') as f:
        print(solve(f))
