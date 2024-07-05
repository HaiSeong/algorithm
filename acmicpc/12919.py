from collections import deque

s = input()
t = input()

queue = deque([s])
visited = {s}

while queue:
    now = queue.popleft()

    if now == t:
        answer = 1
