def countSwitch(number_list):
    count = 0
    
    for i in number_list:
        if i != '':
            count += 1
    return count

s = input()

zero_count = countSwitch(s.split("1"))
one_count = countSwitch(s.split("0"))

if zero_count >= one_count:
    print(one_count)
else:
    print(zero_count)
    