n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

mins = list(map(min, graph))
print(max(mins))
