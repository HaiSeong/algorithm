n = [i for i in map(int, input())]
half_length = len(n)//2

first_half = sum(n[:half_length])
second_half = sum(n[half_length:])

if first_half == second_half:
    print('LUCKY')
else:
    print('READY')