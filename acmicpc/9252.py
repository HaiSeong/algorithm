
a = input()
b = input()

dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

answer = dp[-1][-1]

y = len(a)
x = len(b)
lcs = ''
while len(lcs) < answer:
    if dp[y][x] == dp[y - 1][x]:
        y -= 1
    elif dp[y][x] == dp[y][x - 1]:
        x -= 1
    else:
        lcs += a[y - 1]
        y-=1
        x-=1

print(answer)
print(lcs[::-1])