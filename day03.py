from typing import List
from util import get_input
import time

inp = get_input(3)

t0 = time.perf_counter()
nr = ''

for idx in range(12):
    ones = 0
    zeros = 0
    for x in inp:
        if x[idx] == '1':
            ones += 1
        else:
            zeros += 1
    nr += '1' if ones > zeros else '0'

gamma = int(nr, 2)
epsilon = int(''.join(['1' if x == '0' else '0' for x in nr]), 2)

print('Part 1:')
print(gamma * epsilon)

ox_candidates = inp.copy()
co2_candidates = inp.copy()


def most_common(base: List[str], pos: int, ie: str,  is_lc=False) -> str:
    """Return the most common bit on the given position"""
    ones = 0
    zeros = 0
    for x in base:
        if x[pos] == '1':
            ones += 1
        else:
            zeros += 1
    if ones == zeros:
        return ie
    if is_lc:
        return '1' if ones < zeros else '0'
    else:
        return '1' if ones > zeros else '0'


check_idx = 0
while len(ox_candidates) > 1:
    mc = most_common(ox_candidates, check_idx, '1')
    ox_candidates = [x for x in ox_candidates if x[check_idx] == mc]
    check_idx += 1
ox = int(ox_candidates[0], 2)

check_idx = 0
while len(co2_candidates) > 1:
    mc = most_common(co2_candidates, check_idx, '0', True)
    co2_candidates = [x for x in co2_candidates if x[check_idx] == mc]
    check_idx += 1
co2 = int(co2_candidates[0], 2)

print('Part 2:')
print(ox * co2)

t1 = time.perf_counter() - t0

print(f'time taken: {t1:.6f}s')
