
n = int(input())
lst = list(map(int, input().split()))

dp = [0] * n

dp[n - 1] = 1

for i in range(n-2, -1, -1):
    try:
        dp[i] = dp[i + 1 + lst[i]] + 1
    except:
        dp[i] = 1

print(*dp)