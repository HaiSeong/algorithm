n, m = map(int, input().split())

hands = []
for i in range(1, m + 1):
    h1, h2 = map(int, input().split())
    hands.append((h1, i))
    hands.append((h2, i))

hands.sort()

answer = hands[(n - 1) % len(hands)][1]
print(answer)