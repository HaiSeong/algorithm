
import bisect

n = int(input())
lst = sorted(map(int, input().split()))
m = int(input())
findings = list(map(int, input().split()))

answer = []
for f in findings:
    idx = bisect.bisect_left(lst, f)
    if 0 <= idx < n and lst[idx] == f:
        answer.append("yes")
    else:
        answer.append("no")

print(*answer)
