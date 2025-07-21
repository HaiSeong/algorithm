numbers = input()
answer = 0
for i in range(len(numbers)):
  answer = max(answer + int(numbers[i]), answer * int(numbers[i]))

print(answer)