n, m = map(int, input().split())
a, b, c = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

sums = [[0] * m for _ in range(n)]
sums[0][0] = graph[0][0]
for i in range(1, n):
    sums[i][0] = sums[i - 1][0] + graph[i][0]
for i in range(1, m):
    sums[0][i] = sums[0][i - 1] + graph[0][i]

for i in range(1, n):
    for j in range(1, m):
        sums[i][j] = graph[i][j] + sums[i][j - 1] + sums[i - 1][j] - sums[i - 1][j - 1]



def calculate(y1, x1, y2, x2):
    if y1 == 0 and x1 == 0:
        return sums[y2][x2]
    if y1 == 0:
        return sums[y2][x2] - sums[y2][x1 - 1]
    if x1 == 0:
        return sums[y2][x2] - sums[y1 - 1][x2]

    return sums[y2][x2] - sums[y2][x1 - 1] - sums[y1 - 1][x2] + sums[y1 - 1][x1 - 1]

answer = float('inf')
for i in range(n):
    for j in range(m):
        try:
            cal = calculate(i, j, i + a - 1, j + (b + c) - 1)
            answer = min(answer, cal)
        except:
            break


for i in range(n):
    for j in range(m):
        try:
            cal = calculate(i, j, i + a - 1, j + (c) - 1) + calculate(i + a, j + c, i + a + b -1, j + c + a - 1)
            answer = min(answer, cal)
        except:
            break

for i in range(n):
    for j in range(m):
        try:
            cal = calculate(i, j, i + a - 1, j + (b) - 1) + calculate(i + a, j + b, i + a + c -1, j + b + a - 1)
            answer = min(answer, cal)
        except:
            break


print(answer)
