n = int(input())
dinos = {}
for _ in range(n):
    name = input()
    numAttributes = int(input())
    dinos[name] = [input() for _ in range(numAttributes)]

q = int(input())
for _ in range(q):
    numAttributes = int(input())
    attr = [input() for _ in range(numAttributes)]
    maxScore = 0
    maxDino = ""
    for name in dinos:
        m = sum([1 for x in attr if x in dinos[name]])
        n = numAttributes - m
        k = len(dinos[name])
        score = 100*(m-n)/k
        if score > maxScore:
            maxScore = score
            maxDino = name
    if maxScore >= 50:
        print(maxDino)
    else:
        print("Possible New Discovery")








# n = int(input())
# attributes = {}
# numAttributes = {}
# for _ in range(n):
#     name = input()
#     m = int(input())
#     numAttributes[name] = m
#     for _ in range(m):
#         a = input()
#         if a in attributes: attributes[a].append(name)
#         else: attributes[a] = [name]

# q = int(input())
# for _ in range(q):
#     m = int(input())
#     poss = {}
#     for _ in range(m):
#         a = input()
#         if a not in attributes: continue
#         for dino in attributes[a]:
#             if dino in poss: poss[dino] += 1
#             else: poss[dino] = 1
#     mostLikely = max(poss.keys(), key=lambda x:poss[x])
#     score = 100*(poss[mostLikely]-(m-poss[mostLikely]))/numAttributes[mostLikely]
#     if score >= 50:
#         print(mostLikely)
#     else:
#         print("Possible New Discovery")