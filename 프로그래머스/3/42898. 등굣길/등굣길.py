

    
    
def count(i, j, graph, puddles):
    
    if [ j + 1, i + 1,] in puddles:
        graph[i][j] = 0
        return 0
        
    if i == 0 or j == 0:
        return graph[i][j]
    if graph[i][j] == -1:
        graph[i][j] = (count(i - 1, j, graph, puddles) + count(i, j - 1, graph, puddles)) % 1000000007
    
    return graph[i][j]

def solution(m, n, puddles):
    
    graph = [[-1] * m for _ in range(n)]
    graph[0][0] = 1
    
    g = 1
    for i in range(m):
        if [ i + 1, 0 + 1,] in puddles:
            g = 0
        graph[0][i] = g
    g = 1
    for i in range(n):
        if [ 0 + 1, i + 1,] in puddles:
            g = 0
        graph[i][0] = g
    
    ans = count(n-1, m-1, graph, puddles)
    for g in graph:
        print(g)
    return ans