# 11:44

directions = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}  # 북동남서

n, m = map(int, input().split())
y, x, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
visited[y][x] = True

answer = 1
while True:
    for i in range(4):
        ld = (d + 3) % 4
        ly = y + directions[ld][0]
        lx = x + directions[ld][1]
        d = ld

        if graph[ly][lx] == 0 and not visited[ly][lx]:
            answer += 1
            y, x = ly, lx
            visited[y][x] = True
            break
    else:
        bd = (d + 2) % 4
        by = y + directions[bd][0]
        bx = x + directions[bd][1]
        if graph[by][bx] == 1:
            break
        else:
            y = by
            x = bx

print(answer)