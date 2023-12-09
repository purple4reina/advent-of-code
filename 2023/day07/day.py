def part1(inputs):
    ranks = {k: v for v, k in enumerate('23456789TJQKA')}

    def score(hand):
        hand, _ = hand
        cards = {}
        for card in hand:
            cards[card] = cards.get(card, 0) + 1
        score = sorted(list(cards.values()), reverse=True)
        tie = list(ranks[c] for c in hand)
        return score, tie

    total = 0
    for i, (_, bid) in enumerate(sorted(inputs, key=score)):
        total += bid * (i + 1)

    return total

def part2(inputs):
    values = 'J23456789TQKA'
    ranks = {k: v for v, k in enumerate(values)}

    def score(hand):
        hand, _ = hand
        cards = {}
        js = 0
        for card in hand:
            isj = card == 'J'
            cards[card] = cards.get(card, 0) + (not isj)
            js += isj
        score = sorted(list(cards.get(v, 0) for v in values), reverse=True)
        score[0] += js
        tie = list(ranks[c] for c in hand)
        return score, tie

    total = 0
    for i, (_, bid) in enumerate(sorted(inputs, key=score)):
        total += bid * (i + 1)

    return total

def read_inputs():
    with open('input.txt') as f:
        return f.read().strip()

def process(raw):
    hands = []
    for row in raw.split('\n'):
        hand, bid = row.split()
        hands.append((hand, int(bid)))
    return hands

if __name__ == '__main__':
    read = read_inputs()
    print(part1(process(read)))
    print(part2(process(read)))
