n = int(input())

dp = {}

def count(n):
    if n < 3:
        return 0

    if n in dp:
        return dp[n]

    cases = []

    if n <= 4:
        # 2개로 나누는 경우 -> 1명 구출
        min_chain = (n - 1) // 2
        if (n - 1) % 2 == 1:
            cases.append(1 + count(min_chain) + count(min_chain + 1))
        else:
            cases.append(1 + count(min_chain) * 2)
    else:
        # 3개로 나누는 경우 -> 2명 구출
        min_chain = (n - 2) // 3
        if (n - 2) % 3 == 2:
            cases.append(2 + count(min_chain) * 2 + count(min_chain + 2) * 1)
            cases.append(2 + count(min_chain) * 1 + count(min_chain + 1) * 2)
        elif (n - 2) % 3 == 1:
            cases.append(2 + count(min_chain) * 2 + count(min_chain + 1) * 1)
        else:
            cases.append(2 + count(min_chain) * 3)

    ret = max(cases)
    dp[n] = ret

    return ret


print(count(n))
