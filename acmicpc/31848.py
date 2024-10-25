
n = int(input())
holes = list(map(int, input().split()))
q = int(input())
dotories = list(map(int, input().split()))

for i in range(n):
    holes[i] += i

max_hole = holes[0]
dp = [0] * (max(holes) + 1) # dp[i] : i 크기의 도토리가 떨어질 구멍의 인덱스

for i in range(max_hole + 1):
    dp[i] = 0


for i in range(1, n):
    hole = holes[i]
    if hole > max_hole:
        for j in range(max_hole + 1, hole + 1):
            dp[j] = i
        max_hole = hole

answer = []
for dotory in dotories:
    answer.append(dp[dotory] + 1)

print(*answer)