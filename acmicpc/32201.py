
n = int(input())
before_orders = list(map(int, input().split()))
after_orders = list(map(int, input().split()))

changes = dict()

for order, number in enumerate(before_orders):
    changes[number] = order

for order, number in enumerate(after_orders):
    changes[number] -= order

max_change = max(changes.values())

answer = []
for number in after_orders:
    if changes[number] == max_change:
        answer.append(number)

print(*answer)