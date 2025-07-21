# 못풀었음. 아래는 2차 풀이

s = input()
answer = []
answer.append(len(s))

for step in range(1, len(s) // 2):
  compressed = ""
  prev = s[0:step]
  count = 1

  for i in range(step, len(s), step):
    tmp = s[i: i+step]
    if prev == tmp:
      count += 1
    else:
      if count >= 2:
        compressed += str(count) + prev
      else:
        compressed += prev
      count = 1
      prev = tmp
    if count >= 2:
      compressed += str(count) + prev
    else:
      compressed += prev
  answer.append(len(compressed))

print(min(answer))