
# 36C3 = 36 35 34 // 3 2 1 = 7140
# 5 * 4 * 5 = 100
def combinations(lst, n):
    if n == 0:
        return [[]]

    result = []
    for i, num in enumerate(lst):
        rest = lst[i + 1:]
        for c in combinations(rest, n - 1):
            result.append([num] + c)

    return result

n = int(input())
graph = [list(input().split()) for _ in range(n)]

empties = []
teachers = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'X':
            empties.append((i, j))
        elif graph[i][j] == 'T':
            teachers.append((i, j))

def check():
    for ty, tx in teachers:
        for dy, dx in [(0,-1),(-1,0),(0,1),(1,0)]:
            ny = ty + dy
            nx = tx + dx
            while 0 <= ny < n and 0 <= nx < n:
                if graph[ny][nx] == 'S':
                    return False
                if graph[ny][nx] == 'O':
                    break
                ny += dy
                nx += dx
    return True

answer = False
for case in combinations(empties, 3):
    for i, j in case:
        graph[i][j] = 'O'

    if check():
        answer = True
        break

    for i, j in case:
        graph[i][j] = 'X'

if answer:
    print('YES')
else:
    print('NO')