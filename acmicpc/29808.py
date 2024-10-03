'''


(kor - eng) * 508 : x
(eng - kor) * 108 : y

+

(math - sin) * 212 : z
(sin - math) * 305 : r

= number // 4763 : s

s = x * 508 + z * 212
'''

number = int(input())
if number % 4763 != 0:
    print(0)
    exit(0)
number //= 4763

answer = []
for ke in range(201):
    for ms in range(201):
        if number == 508 * ke + 212 * ms or number == 108 * ke + 212 * ms or number == 508 * ke + 305 * ms or number == 108 * ke + 305 * ms:
            answer.append([ke, ms])

print(len(answer))
for a in answer:
    print(*a)
