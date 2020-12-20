def add(a, b):
    return a + b


def mult(a, b):
    return a * b


def maths(exp):
    total, parens, parens_i, oper = 0, 0, None, add
    for i, char in enumerate(exp):
        if char == " ":
            continue
        elif char == "+":
            if parens == 0:
                oper = add
        elif char == "*":
            if parens == 0:
                oper = mult
        elif char == "(":
            parens += 1
            if parens_i is None:
                parens_i = i
        elif char == ")":
            parens -= 1
            if parens == 0:
                if oper == add:
                    total = oper(total, maths(exp[parens_i+1:i]))
                    parens_i = None
                else:
                    total = oper(total, maths(exp[parens_i:]))
                    break
        else:
            if parens == 0:
                if oper == add:
                    total = oper(total, int(char))
                else:
                    total = oper(total, maths(exp[i:]))
                    break
    return total


def solve(f):
    total = 0
    for line in f:
        total += maths(line)
    return total


if __name__ == '__main__':
    with open('input.txt') as f:
        print(solve([l.strip() for l in f]))
