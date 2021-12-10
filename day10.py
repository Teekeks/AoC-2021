from util import get_input
import time

inp = get_input(10)
t0 = time.perf_counter()
score = 0
line_scores = []


def process_line(line):
    global score
    global line_scores
    stack = []
    ls = 0
    for char in line:
        if char in ('(', '[', '{', '<'):
            stack.append(char)
        else:
            op = stack.pop()
            if char == ')' and op != '(':
                score += 3
                return
            if char == ']' and op != '[':
                score += 57
                return
            if char == '}' and op != '{':
                score += 1197
                return
            if char == '>' and op != '<':
                score += 25137
                return
    while len(stack) > 0:
        op = stack.pop()
        if op == '(':
            ls = ls * 5 + 1
        elif op == '[':
            ls = ls * 5 + 2
        elif op == '{':
            ls = ls * 5 + 3
        elif op == '<':
            ls = ls * 5 + 4
    if ls > 0:
        line_scores.append(ls)


for line in inp:
    process_line(line)

print('Part 1:')
print(score)


line_scores = sorted(line_scores)
print('Part 2:')
print(line_scores[len(line_scores) // 2])

t1 = time.perf_counter() - t0
print(f'time taken: {t1:.6f}s')
