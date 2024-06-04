import sys

input = sys.stdin.readline

n, c = map(int, input().split())
homes = [int(input()) for _ in range(n)]
homes.sort()

def check(dist):
    now = 0
    cnt = 1
    for next in range(1, n):
        if homes[next] - homes[now] >= dist:
            now = next
            cnt += 1

    return cnt >= c


max_dist = homes[-1] - homes[0]

cur = 0
step = max_dist
while step > 0:
    while cur + step <= max_dist and check(cur + step):
        cur += step
    step //= 2
print(cur)

