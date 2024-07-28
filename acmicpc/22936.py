n = int(input())
m = int(input())
lst = [tuple(map(int, input().split())) for _ in range(m)]
start = 0
end_date = max(map(max, lst))

sizes = [0] * (end_date + 1)
for i in range(1, end_date + 1):
    for s, e in lst:
        if s <= i <= e:
            sizes[i] += 1

dp = [0] * (end_date + 1)
dp[1] = sum(sizes[1:n * 7 + 1])
start = 1
max_sizes = dp[1]
for i in range(2, end_date - 7 * n + 2):
    dp[i] = dp[i - 1] + sizes[i + n * 7 - 1] - sizes[i - 1]
    if max_sizes < dp[i]:
        max_sizes = dp[i]
        start = i

answer = m
for s, e in lst:
    for i in range(n - 1):
        if s <= start + 6 + 7 * i and start + 7 + 7 * i <= e:
            answer += 1

# print(sizes)
# print(dp)
print(answer)