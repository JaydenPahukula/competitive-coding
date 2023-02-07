
def value(n):
    string = str(n)
    return int(''.join(sorted(string, reverse=True)))

def cubicPermutations(N):
    scores = {}
    i = 1
    while 1:
        cube = i**3
        v = value(cube)
        if v not in scores:
            scores[v] = [cube]
        else:
            scores[v].append(cube)
            if len(scores[v]) == N:
                return scores[v]
        i += 1


print(cubicPermutations(20))