
SQUARENUMS = [(0,1),(0,4),(0,9),(1,6),(2,5),(3,6),(4,9),(6,4),(8,1)]

def check(chain):
    #change all 9s to 6s in the chains
    for i in range(6):
        if chain[0][i] == 9: chain[0][i] = 6
        if chain[1][i] == 9: chain[1][i] = 6
    #check all nums
    for (a, b) in SQUARENUMS:
        #change all 9s to 6s
        if a == 9: a = 6
        if b == 9: b = 6
        if (a in chain[0] and b in chain[1]) or (a in chain[1] and b in chain[0]):
            continue
        return False
    return True

def solution():
    count = 0
    combs = []
    for a in range(0,10):
        for b in range(a+1, 10):
            for c in range(b+1, 10):
                for d in range(c+1, 10):
                    for e in range(d+1, 10):
                        for f in range(e+1, 10):
                            combs.append([a,b,c,d,e,f])

    for i, c1 in enumerate(combs):
        for c2 in combs[:i]:
            if check([c1,c2]):
                count += 1

    return count

print(solution())