from util import get_input
import time

inp = [int(x) for x in get_input(7)[0].split(',')]
t0 = time.perf_counter()

lf = 1000000000000000000000000


def get_fuel(t: int):
    fuel = 0
    for idx in inp:
        fuel += abs(idx - t)
        if fuel > lf:
            return fuel
    return fuel


for a in range(min(inp), max(inp)):
    f = get_fuel(a)
    if f < lf:
        lf = f
    else:
        break

print('Part 1:')
print(lf)


lf = 1000000000000000000000000


def get_fuel_2(t: int):
    fuel = 0
    for idx in inp:
        steps = abs(idx - t)
        fuel += int((steps * steps + steps) / 2)
        if fuel > lf:
            return fuel
    return fuel


for a in range(min(inp), max(inp)):
    f = get_fuel_2(a)
    if f < lf:
        lf = f
    else:
        break

print('Part 2:')
print(lf)

t1 = time.perf_counter() - t0
print(f'time taken: {t1:.6f}s')
