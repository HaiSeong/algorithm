
line = input()

dp = [0] * (len(line) + 1)
dp[0] = 1

wrong = False
for i in range(1, len(line) + 1):
    flag = True
    if 0 < int(line[i-1]) <= 9:
        dp[i] = dp[i - 1]
        flag = False
    if i - 2 >= 0 and 10 <= int(line[i-2 : i]) <= 26:
        dp[i] += dp[i - 2]
        flag = False
    dp[i] %= 1000000
    if flag:
        wrong = True
        break

if wrong:
    print(0)
else:
    print(dp[-1])