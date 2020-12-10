def solve(f, length=25):
    nums = []
    for line in f:
        num = int(line.strip())
        nums.append(num)

    def findkey():
        def valid(num):
            for a in seen:
                for b in seen:
                    if a == b:
                        break
                    if num == a + b:
                        return True
            return False

        seen = []
        for num in nums:
            if len(seen) < length:
                seen.append(num)
                continue
            if not valid(num):
                return num
            seen.pop(0)
            seen.append(num)

    key = findkey()

    for i, num in enumerate(nums):
        total = [num]
        for add in nums[i+1:]:
            total.append(add)
            if sum(total) == key:
                return max(total) + min(total)
            elif sum(total) > key:
                break


if __name__ == '__main__':
    with open('input.txt') as f:
        print(solve(f))
