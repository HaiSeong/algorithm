import sys

sys.setrecursionlimit(100001)
n = int(input())

dp = [[0] * 3 for _ in range(n + 1)]

empty = 0
left = 1
right = 2

dp[1][empty] = 1
dp[1][left] = 1
dp[1][right] = 1

def count(i, pos):
    if i == 1:
        return 1

    if dp[i][pos] > 0:
        return dp[i][pos]

    if pos == left:
        dp[i][pos] += count(i - 1, empty)
        dp[i][pos] += count(i - 1, right)
    elif pos == right:
        dp[i][pos] += count(i - 1, empty)
        dp[i][pos] += count(i - 1, left)
    else:
        dp[i][pos] += count(i - 1, empty)
        dp[i][pos] += count(i - 1, left)
        dp[i][pos] += count(i - 1, right)
    dp[i][pos] %= 9901
    return dp[i][pos]


ans = count(n, left) + count(n, right) + count(n, empty)
ans %= 9901
print(ans)
