
n = int(input())
m = int(input())
vips = [int(input()) for _ in range(m)]

dp = [1] * (n+1)
dp[1] = 1
if len(dp) > 2:
    dp[2] = 2
"""
1
---------
1 2

2 1
---------
1 2 3
2 1 3

1 3 2
---------
1 2 3 4
2 1 3 4
1 3 2 4

1 2 4 3
2 1 4 3
"""
for i in range(3, n + 1):
    dp[i] = dp[i - 2] + dp[i - 1]

vips.append(0)
vips.append(n+1)
vips.sort()
answer = 1

for i in range(len(vips) - 1):
    answer *= dp[vips[i + 1] - vips[i] - 1]

print(answer)


