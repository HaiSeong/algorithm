import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dots = list(map(int, input().split()))
dots.sort()


def find_start_idx(num):
    cur = -1
    step = len(dots)
    while step > 0:
        while cur + step < len(dots) and dots[cur + step] < num:
            cur += step
        step //= 2

    return cur + 1

def find_end_idx(num):
    cur = -1
    step = len(dots)
    while step > 0:
        while cur + step < len(dots) and dots[cur + step] <= num:
            cur += step
        step //= 2

    return cur

for _ in range(m):
    start, end = map(int, input().split())
    print(find_end_idx(end) - find_start_idx(start) + 1)
