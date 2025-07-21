from collections import Counter

n = int(input())
lst = list(map(int, input().split()))
m = int(input())
findings = list(map(int, input().split()))

answer = []
counter = Counter(lst)
for f in findings:
    if f in counter:
        answer.append("yes")
    else:
        answer.append("no")

print(*answer)
