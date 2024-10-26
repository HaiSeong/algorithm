from collections import deque

n, t = map(int, input().split())
pointings = [0] + list(map(int, input().split()))

queue = deque([(1, 1)])
visited = [0] * (n + 1)

t += 1
while t > 0:
    t -= 1
    now, x = queue.popleft()

    if visited[now] != 0:
        loop_size = x - visited[now]
        t %= loop_size

    visited[now] = x
    queue.append((pointings[now], x + 1))

print(now)