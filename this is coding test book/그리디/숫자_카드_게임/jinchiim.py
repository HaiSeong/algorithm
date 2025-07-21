n,m = map(int, input().split())

for _ in range(n):
    cards = list(map(int, input().split()))
    maxNum = min(cards)

print(maxNum)