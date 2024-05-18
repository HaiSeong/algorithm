import sys

input = sys.stdin.readline

n, k, q, m = map(int, input().split())

sleeping = list(map(int, input().split()))
codes = list(map(int, input().split()))

students = [False] * (n + 3)

for code in codes:
    if code not in sleeping:
        students[code] = True

for i in range(3, n+3):
    if students[i]:
        for j in range(i, n+3, i):
            if j not in sleeping:
                students[j] = True

for _ in range(m):
    s, e = map(int, input().split())
    print(students[s:e+1].count(False))
