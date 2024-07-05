for _ in range(int(input())):

    n, m = map(int, input().split())

    dp = dict()

    # aCb = a-1Cb + a-1Cb-1
    def comb(a, b):
        if b == 0 or a == b:
            return 1

        if (a - 1, b) not in dp:
            dp[(a - 1, b)] = comb(a - 1, b)
        if (a - 1, b - 1) not in dp:
            dp[(a - 1, b - 1)] = comb(a - 1, b - 1)

        return dp[(a - 1, b)] + dp[(a - 1, b - 1)]

    print(comb(m, n))
