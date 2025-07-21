numbers = input()
one = 0
zero = 0

if numbers[0] == "0":
    zero += 1

if numbers[0] == "1":
    one += 1

for i in range(1, len(numbers)):
    if numbers[i-1] != numbers[i]:
        if numbers[i] == "1":
            one += 1
        elif numbers[i] == "0":
            zero += 1

print(min(one, zero))