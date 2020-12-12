import math


class Ferry(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.r = 0

    def N(self, amt):
        self.y += amt

    def S(self, amt):
        self.y -= amt

    def E(self, amt):
        self.x += amt

    def W(self, amt):
        self.x -= amt

    def L(self, amt):
        self.r += amt * math.pi / 180

    def R(self, amt):
        self.r -= amt * math.pi / 180

    def F(self, amt):
        self.x += amt * int(math.cos(self.r))
        self.y += amt * int(math.sin(self.r))

    def manhattan(self):
        return max(self.y, -self.y) + max(self.x, -self.x)


def solve(dirs):
    ferry = Ferry()
    for line in dirs:
        ins, amt = line[0], int(line[1:])
        getattr(ferry, ins)(amt)
    return ferry.manhattan()


if __name__ == '__main__':
    with open('input.txt') as f:
        print(solve(f))
