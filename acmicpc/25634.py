n = int(input())
lst = list(map(int, input().split()))
on = list(map(int, input().split()))
lights = [lst[i] * (on[i] * 2 - 1) for i in range(n)]

# dp[i] i를 오른쪽 끝으로 하는 최소합
dp = [0] * n
dp[0] = lights[0]
for i in range(1, n):
    dp[i] = min(lights[i], lights[i] + dp[i - 1])

# print(lights)
# print(dp)

min_dp = dp[0]
end = 0
for i in range(1, n):
    if min_dp > dp[i]:
        min_dp = dp[i]
        end = i
# print(end)

start = end
tmp = 0
while True:
    tmp += lights[start]
    if tmp == min_dp:
        break
    start -= 1
# print(start)

for i in range(start, end + 1):
    on[i] = (on[i] + 1) % 2

print(sum([lst[i] * on[i] for i in range(n)]))
