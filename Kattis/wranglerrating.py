from collections import defaultdict

n, m = map(int, input().split())

rating = [-1 for _ in range(n+1)]
experience = defaultdict(int)
oldWranglers = set()
newWR = 1500

for _ in range(m):
    winner, loser = map(int, input().split())
    isWinnerNew = winner not in oldWranglers
    isLoserNew = loser not in oldWranglers
    
    if isWinnerNew: rating[winner] = newWR
    if isLoserNew: rating[loser] = newWR

    if -1 in (rating[winner], rating[loser]): exit(1)

    # update rating
    rW, rL = rating[winner], rating[loser]
    rW, rL = max(rW, int((3*rL+rW)//2)), min(rL, int((rW/3+rL)//2))
    # scale
    diffW, diffL = rW-rating[winner], rL-rating[loser]
    eW, eL = experience[winner], experience[loser]
    diffW = int((eL+1)/(eW+eL+2) * diffW)
    diffL = int((eW+1)/(eL+eW+2) * diffL)
    # cap
    diffW, diffL = min(diffW, 1000), min(diffL, 1000)
    diffW, diffL = max(diffW, -1000), max(diffL, -1000) # i think you need this
    rating[winner] += diffW
    rating[loser] += diffL

    print(rating[winner], rating[loser])

    # update newWR
    if isWinnerNew and not isLoserNew: newWR = rating[winner]
    elif isLoserNew and not isWinnerNew: newWR = rating[loser]

    oldWranglers.add(winner)
    oldWranglers.add(loser)
    experience[winner] += 1
    experience[loser] += 1
