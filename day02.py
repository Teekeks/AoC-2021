from util import get_input

inp = get_input(2)

pos = 0
depth = 0

for l in inp:
    d, n = l.split(' ')
    if d == 'forward':
        pos += int(n)
    elif d == 'down':
        depth += int(n)
    else:
        depth -= int(n)

print('part 1:')
print(depth*pos)


pos = 0
depth = 0
aim = 0

for l in inp:
    d, n = l.split(' ')
    if d == 'down':
        aim += int(n)
    elif d == 'up':
        aim -= int(n)
    elif d == 'forward':
        pos += int(n)
        depth += int(n) * aim

print('part 2:')
print(depth*pos)
