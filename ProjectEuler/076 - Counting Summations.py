
def solution(TARGET:int):
    ways = [0 for i in range(TARGET+1)]
    ways[0] = 1

    for i in range(1, TARGET):                
        for j in range(i, TARGET+1):
            ways[j] += ways[j - i]

    return ways[TARGET]

print(solution(100))