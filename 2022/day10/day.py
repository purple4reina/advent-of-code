def part1(inputs):
    cnt = total = 0
    cnt = 1
    val = 1
    vals = [1]
    indexes = (20, 60, 100, 140, 180, 220)
    for cmd in inputs:
        if cmd == 'noop':
            cnt += 1
            vals.append(val)
            if cnt in indexes:
                print('cnt,val,cnt*val: ', cnt,val,cnt*val)
                total += cnt * val
        else:
            cnt += 1
            vals.append(val)
            if cnt in indexes:
                print('cnt,val,cnt*val: ', cnt,val,cnt*val)
                total += cnt * val
            cnt += 1
            print('int(cmd[5:]): ', int(cmd[5:]))
            val += int(cmd[5:])
            vals.append(val)
            if cnt in indexes:
                print('cnt,val,cnt*val: ', cnt,val,cnt*val)
                total += cnt * val
    print('vals: ', vals)
    return total

def part2(inputs):
    pass

def read_inputs():
    import os
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input.txt')
    with open(file) as f:
        return f.read().strip()

def process(raw):
    return raw.split('\n')

if __name__ == '__main__':
    read = read_inputs()
    print(part1(process(read)))
    print(part2(process(read)))
