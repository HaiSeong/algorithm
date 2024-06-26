
n = int(input())
line = input()

stack = []
answer = 0

for c in line:
    if not stack:
        stack.append(c)
    else:
        if stack[-1] == c:
            stack.append(c)
        else:
            stack.pop()
    answer = max(len(stack), answer)

if stack:
    answer = -1

print(answer)
