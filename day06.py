from util import get_input
import time
from pprint import pprint

inp = get_input(6)
t0 = time.perf_counter()

raw_fish = [int(x) for x in inp[0].split(',')]

fish = {i: 0 for i in range(9)}
for sushi in raw_fish:
    fish[sushi] += 1

for day in range(256):
    c_fish = fish.copy()
    fish[0] = c_fish[1]
    fish[1] = c_fish[2]
    fish[2] = c_fish[3]
    fish[3] = c_fish[4]
    fish[4] = c_fish[5]
    fish[5] = c_fish[6]
    fish[6] = c_fish[7] + c_fish[0]
    fish[7] = c_fish[8]
    fish[8] = c_fish[0]

    if day == 79:
        print('Part 1:')
        print(sum(fish.values()))

print('Part 2:')
print(sum(fish.values()))

t1 = time.perf_counter() - t0
print(f'time taken: {t1:.6f}s')
