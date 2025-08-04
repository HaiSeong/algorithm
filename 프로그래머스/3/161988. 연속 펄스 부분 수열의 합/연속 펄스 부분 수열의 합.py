def solution(sequence):
    n = len(sequence)
    dp = [[0] * 2 for _ in range(n)] # i번째 수까지 왔을때 최대 근데 j = 0 이면 + | j = 1이면 -
    
    dp[0][0] = max(sequence[0], 0)
    dp[0][1] = max(-sequence[0], 0)
    
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][1] + sequence[i], sequence[i], 0)
        dp[i][1] = max(dp[i - 1][0] - sequence[i], -sequence[i], 0)
        
    ans = 0
    for d in dp:
        ans = max(ans, max(d))
    
    return ans