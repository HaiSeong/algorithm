n = int(input())

bombs = [input() for _ in range(n)]
counts = [[0] * n for _ in range(n)]


for y in range(n):
    for x in range(n):
        if bombs[y][x] == '*':
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if not (dy == 0 and dx == 0):
                        ny = y + dy
                        nx = x + dx
                        if 0 <= ny < n and 0 <= nx < n:
                             counts[ny][nx] += 1

flag = False
answers = [['.'] * n for _ in range(n)]
for y in range(n):
    line = input()
    for x in range(n):
        if line[x] == 'x' and bombs[y][x] == '*':
            flag = True
            answers[y][x] = '*'
        elif line[x] == 'x':
            answers[y][x] = str(counts[y][x])

for y in range(n):
    for x in range(n):
        if flag and bombs[y][x] == '*':
            answers[y][x] = '*'

for line in answers:
    print(''.join(line))