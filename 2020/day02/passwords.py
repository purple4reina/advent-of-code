def parse_policy(policy):
    nums, letter = policy.split()
    mini, maxi = map(int, nums.split('-'))
    return mini, maxi, letter


def is_valid(policy, passwd):
    mini, maxi, letter = parse_policy(policy)
    cnt = passwd.count(letter)
    return cnt <= maxi and cnt >= mini

def is_valid_2(policy, passwd):
    mini, maxi, letter = parse_policy(policy)
    return sum((passwd[mini-1] == letter, passwd[maxi-1] == letter)) == 1


def get_input():
    pairs = []
    with open('input.txt') as f:
        for line in f:
            pair = line.strip().split(': ')
            pairs.append(pair)
    return pairs


def main():
    passwd_pairs = get_input()
    valid = 0
    for pair in passwd_pairs:
        if is_valid_2(*pair):
            valid += 1
    return valid


if __name__ == '__main__':
    print(main())
