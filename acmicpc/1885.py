import sys
from itertools import permutations

input = sys.stdin.readline

n, k = map(int, input().split())

lst = [int(input()) for _ in range(n)]

parts = [range(1, k + 1)]

for i in range(1, n + 1):
    if k ** i != len(set(permutations(lst, i))):
        print(i)
        break
