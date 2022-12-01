def solve(nums, top=2020):
    spoken = {}
    for i, num in enumerate(nums[:-1]):
        spoken[num] = i

    num = nums[-1]
    while i < top - 2:
        i += 1
        last = spoken.get(num, i)
        spoken[num] = i
        num = i - last

    return num


if __name__ == '__main__':
    nums = (5, 1, 9, 18, 13, 8, 0)
    print(solve(nums, top=30000000))
