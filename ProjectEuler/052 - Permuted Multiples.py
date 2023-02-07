
#checks if a list of iterables are permutations of each other
def isPermutation(lis):
    for n in lis[1:]:
        s = str(lis[0])
        s1 = str(n)
        if len(s1) != len(s): return False
        for c in s1:
            if c not in s: return False
            s = s.replace(c, '', 1)
    return True

#returns the smallest possible x if:  x*1, x*2... x*n  is permutable
def permutedMultiples(n):
    num = 1
    while not isPermutation([num*i for i in range(1,n+1)]):
        num += 1
    return num


print(permutedMultiples(6))



