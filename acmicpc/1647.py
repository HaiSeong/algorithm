import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x: x[2])
parents = [i for i in range(n + 1)]
ranks = [0 for _ in range(n + 1)]

def find(v):
    if parents[v] != v:
        parents[v] = find(parents[v])
    return parents[v]


def union(v1, v2):
    p1 = find(v1)
    p2 = find(v2)
    if ranks[p1] > ranks[p2]:
        parents[p2] = p1
    elif ranks[p1] > ranks[p2]:
        parents[p1] = p2
    else:
        parents[p1] = p2
        ranks[p2] += 1

if n == 2:
    print(0)
    exit(0)

answer = 0
cnt = 0
for v1, v2, cost in edges:
    if find(v1) != find(v2):
        union(v1, v2)
        answer += cost
        cnt += 1
    if cnt == n - 2:
        break

print(answer)
