N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

answer = 0
for i in range(1, M+1):
  if (i % (K+1)) == 0:
    answer += numbers[-2]
  else:
    answer += numbers[-1]

print(answer)