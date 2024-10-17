
dp = [-1] * 11

def pizza_party(n):

    if n <= 1:
        return 0

    if dp[n] > -1:
        return dp[n]

    max_joy = 0
    for i in range(1, n//2 + 1):
        joy = i * (n - i) + pizza_party(i) + pizza_party(n - i)
        max_joy = max(max_joy, joy)
    dp[n] = max_joy
    return max_joy

print(pizza_party(int(input())))