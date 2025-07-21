n = input()
numList = sorted(list(map(int, input().split())), reverse=True)
numSize = numList[0]
count = 0

while numSize <= len(numList) :
    numList = numList[numSize:]
    count += 1
    if numList != []:
        numSize = numList[0]
    
print(count)