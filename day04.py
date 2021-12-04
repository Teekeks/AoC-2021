from util import get_input
import time

inp = get_input(4)
t0 = time.perf_counter()

seq = [int(x) for x in inp[0].split(',')]

boards = []
board = []

# parse input into boards
for line in inp[2:]:
    numbers = line.split(' ')
    if len(numbers) > 1:
        board.append([{'n': int(x), 'h': False} for x in numbers if len(x) > 0])
    else:
        # start new board
        boards.append(board)
        board = []
if len(board) > 0:
    boards.append(board)


def mark_number(nr: int):
    for b in boards:
        for li in b:
            for entry in li:
                if entry['n'] == nr:
                    entry['h'] = True


def get_hit_boards():
    hits = []
    hidx = []
    # check lines
    for idx, b in enumerate(boards):
        for li in b:
            if all([e['h'] for e in li]):
                hits.append(b)
                hidx.append(idx)
    # check columns
    for i, b in enumerate(boards):
        for idx in range(5):
            lv = []
            for li in b:
                lv.append(li[idx]['h'])
            if all(lv):
                hits.append(b)
                hidx.append(i)
    return hits, hidx


# apply numbers
hit = None
sc = None
ltw = None
ltw_s = None

for nr in seq:
    if len(boards) == 1:
        ltw = boards[0]
        ltw_s = nr
        break
    mark_number(nr)
    hits, idxl = get_hit_boards()
    if len(hits) > 0:
        if hit is None:
            hit = hits[0]
            sc = nr
        boards = [b for idx, b in enumerate(boards) if idx not in idxl]


score = 0
for line in hit:
    for entry in line:
        if not entry['h']:
            score += entry['n']

print('Part 1:')
print(score * sc)


score = 0
for line in ltw:
    for entry in line:
        if not entry['h']:
            score += entry['n']

print('Part 2:')
print(score * ltw_s)

t1 = time.perf_counter() - t0

print(f'time taken: {t1:.6f}s')

