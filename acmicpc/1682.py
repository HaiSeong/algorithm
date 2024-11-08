from collections import deque

goal = ''.join(input().split())

queue = deque([('12345678', 0)])
visited = {'12345678'}

answer = 0

while queue:
    s, count = queue.popleft()

    if s == goal:
        answer = count
        break

    next1 = s[::-1]
    next2 = s[3] + s[0] + s[1] + s[2] + s[5] + s[6] + s[7] + s[4]
    next3 = s[0] + s[2] + s[5] + s[3] + s[4] + s[6] + s[1] + s[7]
    next4 = s[4] + s[1] + s[2] + s[3] + s[0] + s[5] + s[6] + s[7]

    for next in [next1, next2, next3, next4]:
        if next not in visited:
            queue.append((next, count + 1))
            visited.add(next)

print(answer)
