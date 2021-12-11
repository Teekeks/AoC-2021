from util import get_input
import time

inp = get_input(11)
t0 = time.perf_counter()

inp = [[int(x) for x in a] for a in inp]

f = 0

for it in range(10000):
    # increase
    for x in range(len(inp)):
        for y in range(len(inp[x])):
            inp[x][y] += 1
    flasher = [[False for _ in range(10)] for _ in range(10)]
    found = True
    while found:
        found = False
        for x in range(len(inp)):
            for y in range(len(inp[x])):
                if inp[x][y] > 9 and not flasher[x][y]:
                    f += 1
                    flasher[x][y] = True
                    found = True
                    if x > 0 and y > 0:
                        inp[x-1][y-1] += 1
                    if x > 0:
                        inp[x-1][y] += 1
                        if y < len(inp[x-1]) - 1:
                            inp[x-1][y+1] += 1
                    if y > 0:
                        inp[x][y-1] += 1
                        if x < len(inp) - 1:
                            inp[x+1][y-1] += 1
                    if x < len(inp) - 1:
                        inp[x+1][y] += 1
                        if y < len(inp[x]) - 1:
                            inp[x+1][y+1] += 1
                    if y < len(inp[x]) - 1:
                        inp[x][y+1] += 1
    if all([all(x) for x in flasher]):
        print('Part 1:')
        print(f)
        print('Part 2:')
        print(it + 1)
        t1 = time.perf_counter() - t0
        print(f'time taken: {t1:.6f}s')
        exit(1)
    # reset all flasher back to 0
    for x in range(len(inp)):
        for y in range(len(inp[x])):
            if inp[x][y] > 9:
                inp[x][y] = 0


