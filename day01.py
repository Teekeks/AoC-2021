from util import get_input

inp = [int(x) for x in get_input(1)]

cur = inp[0]
cnt = 0
for c in inp[1:]:
    if c > cur:
        cnt += 1
    cur = c
print('part 1:')
print(cnt)

cnt = 0
cur = sum(inp[:3])
for idx in range(1, len(inp)-2):
    c = sum(inp[idx:idx+3])
    if c > cur:
        cnt += 1
    cur = c
print('part 2:')
print(cnt)
