n = int(input())
vs = set(map(int, input().split()))
max_i = max(vs)

def count(i):
    if i > max_i:
        return float('inf')

    if i in vs:
        return 0

    return 1 + count(2 * i) + count(2 * i + 1)


answer = count(1)
if answer == float('inf'):
    answer = -1
print(answer)