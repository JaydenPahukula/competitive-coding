# n, m = map(int, input().split())
# canPlay = [set(map(int, input().split()[1:])) for _ in range(n)]
# inverse = {}
# for i in range(n):
#     for note in canPlay[i]:
#         if note in inverse: inverse[note].add(i)
#         else: inverse[note] = {i}
# notes = list(map(int, input().split()))
# possible = list(range(n))
# numSwitches = 0
# for note in notes:
#     newPossible = []
#     for i in possible:
#         if note in canPlay[i]:
#             newPossible.append(i)
#     if newPossible == []:
#         numSwitches += 1
#         possible = inverse[note]
#     else:
#         possible = newPossible
# print(numSwitches)

I=input;N,M=map(int,I().split());R=range(N);a=[set(map(int,I().split()[1:]))for _ in R];l=list(map(int,I().split()));p=list(R);o=0
for n in l:
 p=[i for i in p if n in a[i]]
 if[]==p:o+=1;p={j for j in R if n in a[j]}
print(o)