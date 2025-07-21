
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b.sort(reverse=True)
a += b[:k]
a.sort(reverse=True)
a = a[:n]
print(sum(a))
