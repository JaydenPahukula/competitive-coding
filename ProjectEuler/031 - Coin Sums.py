coins = [100,50,20,10,5,2,1]
target = 200


def findPermutations(t=0, n=0):
    ways = 0
    for i in range(t,target+1,coins[n]):
        if i == target:
            ways += 1
        else:
            if n == 6: continue
            ways += findPermutations(i, n+1)
    return ways


print(findPermutations()+1)
