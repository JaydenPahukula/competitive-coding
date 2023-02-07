
friendList = [i for i in range(1000000)]
branchSize = [1 for i in range(1000000)]
last = []
lasti = 0

def find(id:int):
    if friendList[id] == id:
        return id
    else:
        out = find(friendList[id])
        friendList[id] = out
        return out

def join(a:int, b:int):
    roota = find(a)
    rootb = find(b)
    if roota != rootb:
        #join branches
        friendList[roota] = rootb
        #add the sizes of the branches
        branchSize[rootb] += branchSize[roota]
    return

def getID(k:int):
    global lasti
    if k <= 55:
        id = (100003 - (200003 * k) + (300007 * (k**3))) % 1000000
        last.append(id)
    else:
        #remember the last 55 values and use them here
        id = (last[(lasti-24)%55] + last[lasti]) % 1000000
        last[lasti] = id
        lasti = (lasti+1)%55
    return id

def solution(PM:int, target:float):

    numCalls = 0
    k = -1

    while 1:
        #get call information
        k += 2
        callerID = getID(k)
        calledID = getID(k+1)

        #check if misdial
        if callerID == calledID:
            continue
        
        #join the two branches
        join(callerID, calledID)
        numCalls += 1

        #exit condition
        if (branchSize[find(PM)] / len(friendList)) >= target:
            return numCalls

print(solution(524287, 0.99))