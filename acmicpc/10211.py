

for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    dp = [0] * len(lst) # dp[i] = i를 마지막으로 하는 부분 배열 최대 합

    dp[0] = lst[0]
    for i in range(1, n):
        dp[i] = max(dp[i - 1] + lst[i], lst[i])

    print(max(dp))

