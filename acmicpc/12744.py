from collections import deque

n = int(input())

cakes = []
dirs = []

goal = ''
for i in range(1, n + 1):
    goal += str(i) + '+'

start = ''
for _ in range(n):
    c, d = input().split()
    start += c + d


queue = deque([(start, 0)])
visited = {start}

answer = 0
while queue:
    now, t = queue.popleft()
    # print(now)
    if now == goal:
        answer = t
        break

    for i in range(n + 1):
        tmp = ''
        for j in range(i - 1, -1, -1):
            tmp += now[2*j]
            if now[2*j + 1] == '+':
                tmp += '-'
            else:
                tmp += '+'
        next = tmp + now[2 * i:]
        if next not in visited:
            queue.append((next, t + 1))
            visited.add(next)

print(answer)