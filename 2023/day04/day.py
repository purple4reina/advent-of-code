def part1(inputs):
    total = 0
    for wins, have in inputs:
        val = 0
        for h in have:
            if h in wins:
                val = val * 2 if val else 1
        total += val
    return total

def part2(inputs):
    winning_numbers = len(inputs)
    card_cnts = [1] * winning_numbers
    for card, (wins, have) in enumerate(inputs):
        match_cnt = sum(h in wins for h in have)
        for i in range(card+1, min(card+match_cnt+1, winning_numbers)):
            card_cnts[i] += card_cnts[card]
    return sum(card_cnts)

def read_inputs():
    import os
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    with open(file) as f:
        return f.read().strip()

def process(raw):
    cards = []
    for row in raw.split('\n'):
        _, nums = row.strip().split(': ')
        winning, have = nums.split(' | ')
        winners = []
        while winning:
            winners.append(int(winning[:3].strip()))
            winning = winning[3:]
        haves = []
        while have:
            haves.append(int(have[:3].strip()))
            have = have[3:]
        cards.append((winners, haves))
    return cards

if __name__ == '__main__':
    read = read_inputs()
    print(part1(process(read)))
    print(part2(process(read)))
