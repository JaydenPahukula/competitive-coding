
def permute(array):
    if len(array) == 0:
        return []
    if len(array) == 1:
        return [array]

    l = []
    for i in range(len(array)):
        n = array[i]
        array2 = array[:i] + array[i+1:]
        for p in permute(array2):
           l.append([n] + p)
    return l

def find09Pandigitals():
    permutations = permute([0,1,2,3,4,5,6,7,8,9])
    ints = []
    for p in permutations:
        if p[0] == 0: continue
        s = ""
        for n in p:
            s += str(n)
        ints.append(s)
    return ints


total = 0
for num in find09Pandigitals():
    if int(num[1:4]) % 2 != 0:
        continue
    if int(num[2:5]) % 3 != 0:
        continue
    if int(num[3:6]) % 5 != 0:
        continue
    if int(num[4:7]) % 7 != 0:
        continue
    if int(num[5:8]) % 11 != 0:
        continue
    if int(num[6:9]) % 13 != 0:
        continue
    if int(num[7:10]) % 17 != 0:
        continue
    total += int(num)
print(total)
