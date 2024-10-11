n, r, c = map(int, input().split())

def recur(n, r, c):
    if n < 1:
        return 0

    width = 2 ** (n - 1)

    cnt = recur(n - 1, r % width, c % width)

    if r >= width:
        cnt += (width ** 2) * 2
    if c >= width:
        cnt += width ** 2

    return cnt

print(recur(n, r, c))