for _ in range(int(input())):
    N, M = map(int, input().split())
    room = list(map(int, input().split()))
    numParents = [0 for _ in range(N)]
    children = [[] for _ in range(N)]
    for _ in range(M):
        i, j = map(int, input().split())
        i -= 1
        j -= 1
        numParents[j] += 1
        children[i].append(j)
    
    zeroes = set()
    for task in range(N):
        if numParents[task] == 0:
            zeroes.add(task)

    currRoom = room[0]
    moveCount = 0
    while zeroes:
        for option in zeroes:
            if room[option] == currRoom:
                curr = option
                zeroes.remove(option)
                break
        else:
            #idk what to do here
            moveCount += 1
            currRoom = max([room[task] for task in zeroes], key = [room[task] for task in zeroes].count)
            curr = [task for task in zeroes if room[task] == currRoom][0]

        for nextTask in children[curr]:
            numParents[nextTask] -= 1
            if numParents[nextTask] == 0:
                zeroes.add(nextTask)
    
    print(moveCount)