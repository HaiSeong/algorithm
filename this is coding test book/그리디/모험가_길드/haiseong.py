
n = int(input())
people = list(map(int, input().split()))

people.sort(reverse=True)

answer = 0
max_fear = 0
cnt = 0

while people:
    fear = people.pop()
    cnt += 1
    max_fear = max(max_fear, fear)
    if cnt >= max_fear:
        answer += 1
        max_fear = 0
        cnt = 0

print(answer)