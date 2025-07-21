N = int(input())
people = sorted(list(map(int, input().split())))

answer = 0
party = []

for person in people:
  party.append(person)
  if max(party) == len(party):
    party = []
    answer += 1

print(answer)