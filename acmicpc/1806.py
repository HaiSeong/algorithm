n, m = map(int, input().split())
lst = list(map(int, input().split()))
dp = [0] + lst[:]

for i in range(1, n):
    dp[i + 1] += dp[i]

start = 0
end = 1
answer = float('inf')

while end <= n:
    tmp = dp[end] - dp[start]
    if tmp >= m:
        answer = min(answer, end - start)
        start += 1
    else:
        end += 1

if answer == float('inf'):
    answer = 0
print(answer)
