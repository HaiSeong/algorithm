n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
# dp_max[i][j] : i, j 에서 얻을 수 있는 최대점수
# dp_min[i][j] : i, j 에서 얻을 수 있는 최소점수
dp_max = [-float('inf')] * 3
dp_min = [float('inf')] * 3
dp_max_tmp = [-float('inf')] * 3
dp_min_tmp = [float('inf')] * 3

for j in range(3):
    dp_max[j] = graph[0][j]
    dp_min[j] = graph[0][j]

for i in range(1, n):
    dp_max_tmp[0] = graph[i][0] + max(dp_max[0], dp_max[1])
    dp_max_tmp[1] = graph[i][1] + max(dp_max[0], dp_max[1], dp_max[2])
    dp_max_tmp[2] = graph[i][2] + max(dp_max[1], dp_max[2])
    dp_min_tmp[0] = graph[i][0] + min(dp_min[0], dp_min[1])
    dp_min_tmp[1] = graph[i][1] + min(dp_min[0], dp_min[1], dp_min[2])
    dp_min_tmp[2] = graph[i][2] + min(dp_min[1], dp_min[2])

    for j in range(3):
        dp_max[j] = dp_max_tmp[j]
        dp_min[j] = dp_min_tmp[j]

print(max(dp_max), min(dp_min))
