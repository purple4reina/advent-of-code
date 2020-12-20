import re


def parse(inp):
    rules = {}
    for i, line in enumerate(inp):
        if not line:
            break
        num, rule = line.split(': ')
        rules[num] = '(' + rule.strip('"') + ')'
    rules['8'] = '42 | 42 8'
    rules['11'] = '42 31 | 42 11 31'
    msgs = inp[i+1:]
    return rules, msgs


def conpile(rules):
    rule_0 = '^' + rules['0'] + '$'
    while True:
        m = re.search(r'\d+', rule_0)
        if not m:
            break
        rule_0 = rule_0[:m.start()] + rules[m.group()] + rule_0[m.end():]
    rule_0 = rule_0.replace(' ', '')
    return re.compile(rule_0)


def solve(f):
    rules, msgs = parse(f)
    rule_0 = conpile(rules)

    total = 0
    for msg in msgs:
        if rule_0.match(msg):
            total += 1
    return total


if __name__ == '__main__':
    with open('input.txt') as f:
        print(solve([l.strip() for l in f]))
