import math

def solution(N, checkN, checkD):
    contenders = []
    for d in range(5, N+1):
        if d % checkD == 0:
            continue
        n = math.floor(d * checkN / checkD)
        contenders.append([n, d])

    final = [pair[0]/pair[1] for pair in contenders]
    maxf = 0
    maxi = 0
    for i in range(len(final)):
        if final[i] > maxf:
            maxf = final[i]
            maxi = i

    return contenders[maxi]

print(solution(1000000, 3, 7))