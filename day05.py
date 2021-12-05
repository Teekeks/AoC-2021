from util import get_input
import time

inp = get_input(5)
t0 = time.perf_counter()

# key = 'x,y'
data = {}
# for the first part only
data_1 = {}

for line in inp:
    d = line.split()
    min_val = d[0].split(',')
    max_val = d[-1].split(',')
    min_x = int(min_val[0])
    max_x = int(max_val[0])
    min_y = int(min_val[1])
    max_y = int(max_val[1])

    if min_x == max_x or min_y == max_y:
        if min_x > max_x:
            min_x, max_x = max_x, min_x
        if min_y > max_y:
            min_y, max_y = max_y, min_y
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                key = f'{x},{y}'
                if data.get(key) is None:
                    data[key] = 1
                else:
                    data[key] += 1
                if data_1.get(key) is None:
                    data_1[key] = 1
                else:
                    data_1[key] += 1
    else:
        x = min_x
        y = min_y
        stop_x = max_x + 1 if max_x > min_x else max_x - 1
        stop_y = max_y + 1 if max_y > min_y else max_y - 1
        while x != stop_x and y != stop_y:
            key = f'{x},{y}'
            if data.get(key) is None:
                data[key] = 1
            else:
                data[key] += 1
            if min_x < max_x:
                x += 1
            else:
                x -= 1
            if min_y < max_y:
                y += 1
            else:
                y -= 1
        pass

counter = 0
for key, value in data_1.items():
    if value > 1:
        counter += 1

print('Part 1:')
print(counter)

counter = 0
for key, value in data.items():
    if value > 1:
        counter += 1

print('Part 2:')
print(counter)

t1 = time.perf_counter() - t0
print(f'time taken: {t1:.6f}s')
