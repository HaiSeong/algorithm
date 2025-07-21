s = input()
alpha_list = []
num = 0

for chrac in s:
    if chrac.isalpha():
        alpha_list.append(chrac)
    else:
        num += int(chrac)
        
alpha_list.sort()      

if num != 0:
    alpha_list.append(str(num))

    
print(''.join(alpha_list))