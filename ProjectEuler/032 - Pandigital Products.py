
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

permutations = permute([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("found all permutations of 1-9")



products = []
print("working...")
for p in range(len(permutations)):
    #print("p =", p, "/", len(permutations))
    for i in range(1,5):
        sa = ""
        for a in range(i):
            sa += str(permutations[p][a])
        for j in range(i+1, 8):
            sb = ""
            sc = ""
            for b in range(j-i):
                sb += str(permutations[p][i+b])
            for c in range(9-j):
                sc += str(permutations[p][j+c])
            #print(sa + " * " + sb + " = " + sc)
            if int(sa) * int(sb) != int(sc): continue
            if int(sc) not in products:
                products.append(int(sc))

print(sum(products))
