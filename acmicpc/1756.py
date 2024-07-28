
d, n = map(int, input().split())
widths = list(map(int, input().split()))
pizzas = list(map(int, input().split()))

dp = [float('inf')] * (d + 1)

for i in range(d):
    dp[i + 1] = min(widths[i], dp[i])

answer = 0
i_dp = d + 1
for pizza in pizzas:
    i_dp -= 1
    while i_dp > 0:
        if dp[i_dp] >= pizza:
            break
        i_dp -= 1
print(max(i_dp, 0))

