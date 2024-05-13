n = int(input())
small = []
big = []
for _ in range(n - 1):
    s, b = map(int, input().split())
    small.append(s)
    big.append(b)
k = int(input())

# dp[i][0] : i까지 왔는데 k를 사용하지 않은 최소 에너지
# dp[i][1] : i까지 왔는데 k를 사용한 최소 에너지
# dp[i][0] = min(dp[i-1][0] + small[i-1], dp[i-2][0] + big[i-2])
# dp[i][1] = min(dp[i-3][0] + k, dp[i-1][1] + small[i-1], dp[i-2][1] + big[i-2])

dp = [[0] * 2 for _ in range(n)]
if n == 1:
    print(0)
    exit(0)
if n == 2:
    print(small[0])
    exit(0)
if n == 3:
    print(min(small[0] + small[1], big[0]))
    exit(0)

dp[1][0] = small[0]
dp[2][0] = min(dp[1][0] + small[1], dp[0][0] + big[0])
dp[0][1] = float('inf')
dp[1][1] = float('inf')
dp[2][1] = float('inf')

for i in range(3, n):
    dp[i][0] = min(dp[i - 1][0] + small[i - 1], dp[i - 2][0] + big[i - 2])
    dp[i][1] = min(dp[i - 3][0] + k, dp[i - 1][1] + small[i - 1], dp[i - 2][1] + big[i - 2])

print(min(dp[n - 1]))
