from collections import defaultdict

n = int(input())
stocked = defaultdict(list)
for _ in range(int(input())):
    store, item = input().split()
    stocked[item].append(int(store))
items = [input() for _ in range(int(input()))]

# get min path
impossible = False
minPath = []
for item in items:
    for store in sorted(stocked[item]):
        if not minPath or store >= minPath[-1]:
            minPath.append(store)
            break
    else:
        impossible = True
        break

if impossible:
    print("impossible")
else:
    # get max path
    maxPath = []
    for item in items[::-1]:
        for store in sorted(stocked[item], reverse=True):
            if not maxPath or store <= maxPath[-1]:
                maxPath.append(store)
                break
    
    # compare
    if minPath == maxPath[::-1]:
        print("unique")
    else:
        print("ambiguous")

        




# # WA:(
# unique = True
# currStores = {0}
# for _ in range(int(input())):
#     item = input()
#     nextStores = set()
#     for currStore in currStores:
#         for stockedStore in stocked[item]:
#             if stockedStore >= currStore:
#                 if unique and stockedStore in nextStores:
#                     unique = False
#                 else:
#                     nextStores.add(stockedStore)
#     if len(nextStores) == 0:
#         print("impossible")
#         break
#     currStores = nextStores.copy()
# else:
#     if unique:
#         print("unique")
#     else:
#         print("ambiguous")