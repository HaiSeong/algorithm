'''
103000509
002109400
000704000
300502006
060000050
700803004
000401000
009205800
804000107
'''

graph = [list(map(int, list(input()))) for _ in range(9)]

lst = []
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            lst.append((i, j))

visited = set()


def check(y, x):
    visited.clear()
    for i in range(9):
        if graph[y][i] == 0:
            continue
        if graph[y][i] in visited:
            return False
        visited.add(graph[y][i])
    visited.clear()
    for i in range(9):
        if graph[i][x] == 0:
            continue
        if graph[i][x] in visited:
            return False
        visited.add(graph[i][x])
    visited.clear()
    for i in range(y // 3 * 3, y // 3 * 3 + 3):
        for j in range(x // 3 * 3, x // 3 * 3 + 3):
            if graph[i][j] == 0:
                continue
            if graph[i][j] in visited:
                return False
            visited.add(graph[i][j])

    return True


def get_next(y, x):
    nexts = set([i for i in range(graph[y][x] + 1, 10)])
    already = set()
    for i in range(9):
        already.add(graph[y][i])
        already.add(graph[i][x])
    for i in range(y // 3 * 3, y // 3 * 3 + 3):
        for j in range(x // 3 * 3, x // 3 * 3 + 3):
            already.add(graph[i][j])
    return min(nexts.difference(already))


answer = False


def bt(depth):
    if depth >= len(lst):
        for g in graph:
            for c in g:
                print(c, end='')
            print()
        exit(0)

    y, x = lst[depth]

    while True:
        try:
            graph[y][x] = get_next(y, x)
        except:
            break
        bt(depth + 1)
    graph[y][x] = 0


bt(0)
