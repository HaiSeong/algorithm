import sys

input = sys.stdin.readline

v, e = map(int, input().split())

edges = []
for _ in range(e):
    edges.append(tuple(map(int, input().split())))

edges.sort(key=lambda x: x[2])

answer = 0
linked = set()
for a, b, cost in edges:
    if cost > 0 and a in linked and b in linked:
        continue

    answer += cost
    linked.add(a)
    linked.add(b)

    if cost > 0 and len(linked) == v:
        break

print(answer)