from collections import deque

n, k = map(int, input().split())
belts = deque(map(int, input().split()))
robots = deque([0] * (2 * n))

answer = 1
while True:
    # 1
    belts.appendleft(belts.pop())
    robots.appendleft(robots.pop())

    # 2
    robots[n - 1] = 0
    for i in range(n - 2, -1, -1):
        if robots[i] == 1 and robots[i + 1] == 0 and belts[i + 1] > 0:
            belts[i + 1] -= 1
            robots[i + 1] += 1
            robots[i] = 0
    robots[n - 1] = 0

    # 3
    if belts[0] > 0: # and robots[0] == 0:
        robots[0] += 1
        belts[0] -= 1

    # 4
    if len([b for b in belts if b <= 0]) >= k:
        break

    answer += 1

print(answer)