# n * r = 100 * 10000

n, m, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = [['S'] * m for _ in range(n)]
attacks = []
defends = []
for _ in range(r):
    a = tuple(input().split())
    attacks.append((int(a[0]), int(a[1]), a[2]))
    defends.append(tuple(map(int, input().split())))

dirs = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}

point = 0

def broke(y, x, d):
    global point
    if answer[y][x] == 'F':
        return

    dy, dx = dirs[d]
    for i in range(graph[y][x] - 1, 0, -1):
        ny, nx = y + dy * i, x + dx * i
        if 0 <= ny < n and 0 <= nx < m:
            broke(ny, nx, d)
    answer[y][x] = 'F'
    point += 1

for t in range(r):
    y, x, d = attacks[t]
    y -= 1
    x -= 1
    broke(y, x, d)
    y, x = defends[t]
    y -= 1
    x -= 1
    answer[y][x] = 'S'


print(point)
for a in answer:
    print(*a)

