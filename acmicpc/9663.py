n = int(input())
queens = [-1] * n
answer = 0

def dfs(depth):
    global answer

    if depth == n:
        answer += 1
        return

    for i in range(n):
        queens[depth] = i
        y1 = i
        x1 = depth
        for j in range(depth):
            y2 = queens[j]
            x2 = j

            if y1 == y2:
                break
            if x1 == x2:
                break
            if y1 - y2 == x1 - x2:
                break
            if y1 - y2 == x2 - x1:
                break
        else:
            dfs(depth + 1)

dfs(0)
print(answer)
