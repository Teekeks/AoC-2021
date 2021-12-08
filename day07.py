from util import get_input
import time

inp = [int(x) for x in get_input(7)[0].split(',')]
t0 = time.perf_counter()

n = len(inp)
inp = sorted(inp)
median = inp[int(n/2)]
print('Part 1:')
print(sum([abs(i - median) for i in inp]))
mean = int(sum(inp) / n)
print('Part 2:')
print(min([int(sum([i * (i + 1) / 2 for i in [abs(a - m) for a in inp]])) for m in range(mean - 1, mean + 2)]))

t1 = time.perf_counter() - t0
print(f'time taken: {t1:.6f}s')
