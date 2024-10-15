
n, k = map(int, input().split())
password = list(input())

costs = {'A': 0}
for i in range(ord('B'), ord('Z') + 1):
    costs[chr(i)] = ord('Z') + 1 - i

for i in range(n):
    p = password[i]
    if costs[p] <= k:
        k -= costs[p]
        password[i] = 'A'

password[-1] = chr((ord(password[-1]) - ord('A') + k) % (ord('Z') - ord('A') + 1) + ord('A'))

print(''.join(password))
