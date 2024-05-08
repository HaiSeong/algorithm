import heapq
import sys

input = sys.stdin.readline

n = int(input())

smalls = []
mid = int(input())
larges = []

print(mid)
for length in range(1, n):
    i = int(input())

    if i <= mid:
        heapq.heappush(smalls, -i)
    else:
        heapq.heappush(larges, i)

    # [1, 2, 3]  [4, 5, 6]
    if len(smalls) > len(larges):
        heapq.heappush(larges, mid)
        mid = -heapq.heappop(smalls)
    elif len(smalls) + 1 < len(larges):
        heapq.heappush(smalls, -mid)
        mid = heapq.heappop(larges)

    print(mid)
