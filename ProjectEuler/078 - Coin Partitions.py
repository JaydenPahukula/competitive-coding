
def piles(n:int):
    ways = [0 for x in range(n+1)]
    ways[0] = 1

    for i in range(1, n+1):                
        for j in range(i, n+1):
            ways[j] += ways[j - i]
    return ways[n]

def solution(t:int):
    n = 2
    while 1:
        p = piles(n)
        print(n, p, p%t)
        if p % t == 0:
            break
        else:
            n += 1
    return n

print(solution(1000000))