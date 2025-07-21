n, m, k = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort(reverse=True)

first = lst[0]
second = lst[1]

cnt_second = m // (k + 1)
cnt_first = m - cnt_second

answer = cnt_first * first + cnt_second * second
print(answer)
