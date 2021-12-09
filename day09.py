from util import get_input
import time
from pprint import pprint

inp = [[int(a) for a in x] for x in get_input(9)]
t0 = time.perf_counter()

low_points = []
max_y = 99
max_x = len(inp) - 1

for x in range(len(inp)):
    for y in range(len(inp[x])):
        cur = inp[x][y]
        if x == 0 or inp[x-1][y] > cur:
            if x == len(inp) - 1 or inp[x+1][y] > cur:
                if y == 0 or inp[x][y-1] > cur:
                    if y == len(inp[x]) - 1 or inp[x][y+1] > cur:
                        low_points.append((cur, x, y))

        pass
print('Part 1:')
print(sum([x[0]+1 for x in low_points]))


# flood fill

used_points = [f'{x[1]}/{x[2]}' for x in low_points]
basins = [[{'x': x[1], 'y': x[2]}] for x in low_points]


def get_points(x, y):
    p = []
    if x > 0 and f'{x-1}/{y}' not in used_points:
        p.append({'x': x-1, 'y': y})
        used_points.append(f'{x-1}/{y}')

    if x < max_x and f'{x+1}/{y}' not in used_points:
        p.append({'x': x+1, 'y': y})
        used_points.append(f'{x+1}/{y}')

    if y > 0 and f'{x}/{y-1}' not in used_points:
        p.append({'x': x, 'y': y-1})
        used_points.append(f'{x}/{y-1}')

    if y < max_y and f'{x}/{y+1}' not in used_points:
        p.append({'x': x, 'y': y+1})
        used_points.append(f'{x}/{y+1}')
    return p


for basin in basins:
    start = basin[0]
    flood = get_points(start['x'], start['y'])
    # start the flood
    while len(flood) > 0:
        cur = flood.pop()
        if inp[cur['x']][cur['y']] != 9:
            basin.append(cur)
            flood += get_points(cur['x'], cur['y'])

basins = sorted(basins, key=len)
print('Part 2:')
print(len(basins[-1]) * len(basins[-2]) * len(basins[-3]))

t1 = time.perf_counter() - t0
print(f'time taken: {t1:.6f}s')
