from util import get_input
import time

inp = get_input(8)
t0 = time.perf_counter()

counter = 0
c2 = 0

for line in inp:
    v = line.split()
    v_in = v[:10]
    v_out = v[-4:]
    mapping = ['' for _ in range(10)]
    sig = sorted(v_in, key=len)
    for s in sig:
        if len(s) == 2:
            mapping[1] = s
        elif len(s) == 3:
            mapping[7] = s
        elif len(s) == 4:
            mapping[4] = s
        elif len(s) == 5:
            if all([c in s for c in mapping[1]]):
                mapping[3] = s
            elif sum([c in s for c in mapping[4]]) == 3:
                mapping[5] = s
            else:
                mapping[2] = s
        elif len(s) == 6:
            if all([c in s for c in mapping[4]]):
                mapping[9] = s
            elif all([c in s for c in mapping[7]]):
                mapping[0] = s
            else:
                mapping[6] = s
        else:
            mapping[8] = s

    on = ''
    for vo_digit in v_out:
        # part 1
        if len(vo_digit) in (2, 3, 4, 7):  # 1, 7, 4, 8
            counter += 1
        # part 2
        for idx in range(10):
            if all([c in vo_digit for c in mapping[idx]]) and len(mapping[idx]) == len(vo_digit):
                on += str(idx)
    c2 += int(on)


print('Part 1:')
print(counter)

print('Part 2:')
print(c2)


t1 = time.perf_counter() - t0
print(f'time taken: {t1:.6f}s')
