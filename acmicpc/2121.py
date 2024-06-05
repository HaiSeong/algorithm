import sys

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())

dots = set()
for _ in range(n):
    x, y = map(int, input().split())
    dots.add((x, y))

answer = 0
for x, y in dots:
    if (x + a, y) in dots and (x, y + b) in dots and (x + a, y + b) in dots:
        answer += 1

print(answer)

