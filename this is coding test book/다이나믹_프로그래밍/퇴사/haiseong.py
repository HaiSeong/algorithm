
from collections import deque

n = int(input())
T = []
P = []
for _ in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
T.append(float("inf"))
P.append(0)

def dfs(start):
    stack = deque([(start, 0)])

    answer = 0
    while stack:
        now, money = stack.pop()
        if now <= n:
            answer = max(answer, money)

            for next, got in [(now + 1, 0), (now + T[now], P[now])]:
                    stack.append((next, money + got))


    return answer

print(dfs(0))


