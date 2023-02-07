import math

def solution(fileName:str):
    #read file
    with open(fileName, 'r') as f:
        pairs = f.readlines()

    final = {}
    for i in range(len(pairs)):
        pairs[i] = [int(x) for x in pairs[i].split(',')]
        final[pairs[i][1] * math.log(pairs[i][0], 10)] = i

    return final[max(final)] + 1


print(solution("099 - base_exp.txt"))
