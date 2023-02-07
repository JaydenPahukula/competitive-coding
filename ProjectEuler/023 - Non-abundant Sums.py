s = 0
n = 28

def divisors(num):
    list = [1]
    for i in range(2,int(num/2)+1):
        if num % i == 0:
            list.append(i)
    return list

def isAbundant(num):
    if sum(divisors(num)) > num:
        return True
    return False

abundantNums = []
l = []
for i in range(1,28124):
    if isAbundant(i):
        abundantNums.append(i)
    l.append(i)

for i in range(len(abundantNums)):
    for j in range(i, len(abundantNums)):
        abundantSum = abundantNums[i]+abundantNums[j]
        if abundantSum < 28124 and abundantSum in l:
            l.remove(abundantSum)

print(sum(l))


#tried:
#391285755
#4179805






