def part1(rocks):
    world = {}
    for path in rocks:
        endx, endy = path.pop(0)
        while path:
            (startx, starty), (endx, endy) = (endx, endy), path.pop(0)
            stepx = 2*(endx > startx) - 1
            stepy = 2*(endy > starty) - 1
            for x in range(startx, endx+stepx, stepx):
                for y in range(starty, endy+stepy, stepy):
                    world[(x, y)] = True

    rockx, rocky, count = 500, 0, 0
    while True:
        # if in infinite pit, break
        if rocky > 999:
            return count

        # fall down
        elif (rockx, rocky + 1) not in world:
            rockx, rocky = rockx, rocky + 1

        # fall diagonal left
        elif (rockx - 1, rocky + 1) not in world:
            rockx, rocky = rockx - 1, rocky + 1

        # fall diagonal right
        elif (rockx + 1, rocky + 1) not in world:
            rockx, rocky = rockx + 1, rocky + 1

        # else stop, next rock
        else:
            world[(rockx, rocky)] = True
            rockx, rocky, count = 500, 0, count + 1

def part2(rocks):
    world, maxy = {}, 0
    for path in rocks:
        endx, endy = path.pop(0)
        while path:
            (startx, starty), (endx, endy) = (endx, endy), path.pop(0)
            stepx = 2*(endx > startx) - 1
            stepy = 2*(endy > starty) - 1
            for x in range(startx, endx+stepx, stepx):
                for y in range(starty, endy+stepy, stepy):
                    world[(x, y)] = True
                    maxy = max(maxy, y)

    rockx, rocky, count = 500, 0, 0
    while True:
        # if in infinite pit, break
        if rocky == maxy + 1:
            world[(rockx, rocky)] = True
            rockx, rocky, count = 500, 0, count + 1

        # fall down
        elif (rockx, rocky + 1) not in world:
            rockx, rocky = rockx, rocky + 1

        # fall diagonal left
        elif (rockx - 1, rocky + 1) not in world:
            rockx, rocky = rockx - 1, rocky + 1

        # fall diagonal right
        elif (rockx + 1, rocky + 1) not in world:
            rockx, rocky = rockx + 1, rocky + 1

        # else stop, next rock
        else:
            world[(rockx, rocky)] = True
            if rockx == 500 and rocky == 0:
                break
            rockx, rocky, count = 500, 0, count + 1

    return count + 1

def read_inputs():
    import os
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    with open(file) as f:
        return f.read().strip()

def process(raw):
    rocks = []
    for path in raw.split('\n'):
        if not path:
            break
        rock = []
        for loc in path.split(' -> '):
            rock.append(eval(loc))
        rocks.append(rock)
    return rocks

if __name__ == '__main__':
    read = read_inputs()
    print(part1(process(read)))
    print(part2(process(read)))
