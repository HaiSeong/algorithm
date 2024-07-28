import sys

input = sys.stdin.readline

n, m = map(int, input().split())
times = [int(input()) for _ in range(n)]

cur = 0
max = 10**9 * 1000000000
step = max


def check(time):
    global m

    cnt = 0
    for t in times:
        cnt += time // t
    return m <= cnt


while step > 0:
    while cur + step <= max and not check(cur + step):
        cur += step
    step //= 2

print(cur + 1)

