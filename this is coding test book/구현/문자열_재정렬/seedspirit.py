numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
num = []
string = []

user_input = input()

for i in user_input:
  if i in numbers:
    num.append(i)
  else:
    string.append(i)

string.sort()

answer =""
for i in string:
  answer += i

num_sum = 0
for n in num:
  num_sum += int(n)

answer = answer + str(num_sum)
print(answer)