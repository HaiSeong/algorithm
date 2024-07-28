import sys

sys.setrecursionlimit(100000)

r, c = list(map(int, input().split()))
graph = [list(input()) for _ in range(r)]

root = set()
answer = 0


def dfs(y, x):
    global answer
    print(root)

    if graph[y][x] in root:
        answer = max(answer, len(root))
        return
    root.add(graph[y][x])

    for dy, dx in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
        ny = dy + y
        nx = dx + x
        if 0<=ny<r and 0<=nx<c:
            dfs(ny, nx)
            root.remove(graph[ny][nx])

dfs(0, 0)
print(answer)