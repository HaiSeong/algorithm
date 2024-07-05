n = int(input())

graph = [['*'] * n for _ in range(n)]


def make_hole(y, x, width):
    if width == 1:
        return

    for i in range(width // 3, width // 3 * 2):
        for j in range(width // 3, width // 3 * 2):
            graph[y + i][x + j] = ' '

    for i in range(3):
        for j in range(3):
            make_hole(y + width // 3 * i, x + width // 3 * j, width // 3)


make_hole(0, 0, n)

for g in graph:
    print(''.join(g))
