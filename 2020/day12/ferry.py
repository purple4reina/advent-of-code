import math


class Ferry(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.waypoint_x = 10
        self.waypoint_y = 1

    def N(self, amt):
        self.waypoint_y += amt

    def S(self, amt):
        self.waypoint_y -= amt

    def E(self, amt):
        self.waypoint_x += amt

    def W(self, amt):
        self.waypoint_x -= amt

    def L(self, amt):
        while amt:
            self.waypoint_x, self.waypoint_y = -self.waypoint_y, self.waypoint_x
            amt -= 90

    def R(self, amt):
        while amt:
            self.waypoint_x, self.waypoint_y = self.waypoint_y, -self.waypoint_x
            amt -= 90

    def F(self, amt):
        self.x += amt * self.waypoint_x
        self.y += amt * self.waypoint_y

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
