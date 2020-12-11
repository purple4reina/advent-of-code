def cache(fn):
    _cache = {}
    def wrap(*args):
        if args in _cache:
            return _cache[args]
        ret = fn(*args)
        _cache[args] = ret
        return ret
    return wrap


def solve(f):
    nums = []
    for line in f:
        nums.append(int(line))
    nums.sort()
    last = nums[-1] + 3

    @cache
    def search(prev, index):
        if index >= len(nums):
            if last - prev > 3:
                return False
            return True

        num = nums[index]
        if num - prev > 3:
            return False

        return dig(num, index+1)

    def dig(num, index):
        totals = 0
        for i in range(index, len(nums)+1):
            total = search(num, i)
            if not total:
                break
            totals += total
        return totals

    return dig(0, 0)


if __name__ == '__main__':
    with open('input.txt') as f:
        print(solve(f))
