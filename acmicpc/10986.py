
n, m = map(int, input().split())
lst = list(map(int, input().split()))
dp = lst[:]
for i in range(1, n):
    dp[i] += dp[i - 1]

answer = 0
for i in range(n):
    if dp[i] % m == 0:
        answer += 1
    for j in range(i):
        if (dp[i] - dp[j]) % m == 0:
            answer += 1

print(answer)

