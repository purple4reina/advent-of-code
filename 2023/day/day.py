def part1(inputs):
    reds, blues, greens = 12, 14, 13
    total = 0
    for i, game in enumerate(inputs):
        for red, blue, green in game:
            if red > reds or blue > blues or green > greens:
                break
        else:
            total += i + 1
    return total

def part2(inputs):
    pass

def read_inputs():
    import os
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    with open(file) as f:
        return f.read().strip()

def process(raw):
    games = []
    for row in raw.split('\n'):
        _, pulls = row.split(':')
        gamepulls = []
        for game in pulls.split(';'):
            gameballs = [0, 0, 0]
            for colors in game.split(','):
                num, color = colors.strip().split(' ')
                num = int(num.strip())
                color = color.strip()
                if color == 'red':
                    gameballs[0] += num
                elif color == 'blue':
                    gameballs[1] += num
                elif color == 'green':
                    gameballs[2] += num
            gamepulls.append(gameballs)
        games.append(gamepulls)
    return games

if __name__ == '__main__':
    read = read_inputs()
    print(part1(process(read)))
    print(part2(process(read)))
