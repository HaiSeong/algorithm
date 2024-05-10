
n = int(input())

dp = [0] * 50001
dp[1] = 1

for i in range(2, n + 1):
    count = 4
    j = 1
    while i - j * j >= 0:
        count = min(count, dp[i - j * j])
        j += 1
    dp[i] = count + 1

print(dp[n])

