from collections import deque

n, m = map(int ,input().split())
lst = list(map(int, input().split()))

hamster = deque()
weight = 0
answer = 0

for a in lst:
    hamster.append(a) # 일단 다음 구멍 먹기
    weight += a
    while weight > m: # 부피 최대 초과하면 뱉기
        pop = hamster.popleft()
        weight -= pop

    answer = max(answer, weight) # 답 비교

print(answer)
