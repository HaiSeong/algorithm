def solution(sticker):
    
    n = len(sticker)
    dp = [[[0] * 2 for _ in range(2)] for _ in range(n)] 
    # dp[i][j][k] : i번째 스티커를 찢었으면 j = 1 아니면 j = 0 일때 최대 점수 , k = 0 이면 처음꺼 안뜯음 1이면 뜯음
    
    dp[0][0][0] = 0
    dp[0][1][1] = sticker[0]
    dp[0][0][1] = -float('inf')
    dp[0][1][0] = -float('inf')
    
    for i in range(1, n - 1):
        dp[i][0][0] = max(dp[i-1][0][0], dp[i-1][1][0])
        dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][1][1])
        
        dp[i][1][0] = dp[i-1][0][0] + sticker[i]
        dp[i][1][1] = dp[i-1][0][1] + sticker[i]
    
    i = n-1
    dp[i][0][0] = max(dp[i-1][1][0], dp[i-1][0][0]) # 처음꺼 안뜯고 이번도 안뜯기
    dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][1][1]) # 처음거 뜯음 이번에 안뜯기
    dp[i][1][0] = dp[i-1][0][0] + sticker[i] # 처음거 안뜯음 이번엔 뜯기
    

    return max(max(dp[n-1][0]), max(dp[n-1][1]))