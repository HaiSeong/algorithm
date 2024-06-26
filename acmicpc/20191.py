s = input()
t = input()


# dp[i][c] : i번 이후에 t에서 c가 등장하는 index

len_tn = len(s) * len(t)
dp = [[-1] * (ord('z') - ord('a') + 1) for _ in range(len_tn)]

i = 0
while i < len_tn:
    j = i
    while j >= 0:
        if dp[j][ord(t[i % len(t)]) - ord('a')] != -1:
            break
        dp[j][ord(t[i % len(t)]) - ord('a')] = i
        j-=1
    i+=1

idx = 0
if dp[0][ord(s[0]) - ord('a')] == 0:
    idx = dp[0][ord(s[0]) - ord('a')]
for c in s[1:]:
    idx = dp[idx + 1][ord(c) - ord('a')]
    if idx == -1:
        print(-1)
        exit(0)

print((idx + len(t)) // len(t))
