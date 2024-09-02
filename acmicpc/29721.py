
n, k = map(int, input().split())
dibabas = {tuple(map(int, input().split())) for _ in range(k)}

answer = set()

for x, y in dibabas:
    for dx, dy in [(0,-2),(-2,0),(0,2),(2,0)]:
        nx = x + dx
        ny = y + dy

        if 0<nx<=n and 0<ny<=n:
            answer.add((nx, ny))

answer = answer.difference(dibabas)

print(len(answer))