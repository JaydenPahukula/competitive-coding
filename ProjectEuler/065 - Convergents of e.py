import math

def econvergents(j:int):

    #calculate a
    #this is dumb i know
    a = [1] * j
    a[0] = 2
    k = 2
    for i in range(1, j):
        if (i+1) % 3 == 0:
            a[i] = k
            k += 2

    #find fraction
    top = 1
    bottom = a[-1]
    for i in range(len(a)-2, -1, -1):
        #add a[i] to fraction
        top += bottom * a[i]
        #flip fraction
        top, bottom = bottom, top

    #return sum
    s = 0
    for c in str(bottom):
        s += int(c)
    return s

print(econvergents(100))