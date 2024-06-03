
n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

answer = []

def dfs(depth, idx, nums):

    if depth == m:
        answer.append(nums)
        return

    for next_idx in range(idx + 1, n):
        dfs(depth + 1, next_idx, nums[:] + [lst[next_idx]])

for i in range(n):
    dfs(1, i, [lst[i]])

for a in answer:
    print(*list(map(str, a)))
