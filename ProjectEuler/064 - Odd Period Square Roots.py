import math


def findPattern(n):
    # the amount of times a pattern needs to repeat to be confirmed
    REQUIREMENT = 10
    
    a = [0]
    a[0] = math.floor(math.sqrt(n))
    x = a[0]
    numer = 1
    i = 1
    patterns = []

    while 1:

        #calculate a[i]
        denom = (n - x**2) / numer
        group = (x + math.sqrt(n)) / denom
        a.append(0)
        a[i] = math.floor(group)
        x = abs(x - (denom*a[i]))
        numer = denom


        #check patterns
        for pattern in patterns:
            #skip failed patterns
            if pattern[1] == -1:
                continue
            if a[i] == pattern[0][(i-1) % len(pattern[0])]:
                #success
                pattern[1] += 1
                #return condition
                if pattern[1] == REQUIREMENT:
                    return [a[0], pattern[0]]
            else:
                #failed
                pattern[1] = -1

        #look for new patterns
        if a[i] == a[1]:
            if i == 1:
                patterns.append([[a[1]], 0])
            else:
                patterns.append([a[1:i], 0])

        #increment
        i += 1

    return "something went wrong"

def oddPeriodSquareRoots(N):
    count = 0

    for num in range(2, N+1):

        #skip square numbers
        if math.sqrt(num) % 1 == 0:
            continue

        pattern = findPattern(num)[1]
        if len(pattern) % 2 == 1:
            count += 1

    return count

print(oddPeriodSquareRoots(10000))
