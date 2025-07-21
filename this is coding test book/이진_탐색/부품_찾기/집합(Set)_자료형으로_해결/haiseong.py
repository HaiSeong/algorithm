n = int(input())
lst = set(map(int, input().split()))
m = int(input())
findings = list(map(int, input().split()))

answer = []
for f in findings:
    if f in lst:
        answer.append("yes")
    else:
        answer.append("no")

print(*answer)
