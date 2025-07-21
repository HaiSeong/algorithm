
n = int(input())
students = []
for _ in range(n):
    name, kor, math, eng = input().split()
    kor = int(kor)
    math = int(math)
    eng = int(eng)
    students.append((kor, math, eng, name))

students.sort(key = lambda s : (-s[0], s[1], -s[2], s[3]))

for s in students:
    print(s[3])