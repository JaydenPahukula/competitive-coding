D = {"lower":0, "middle":1, "upper":2}
for _ in range(int(input())):
    n = int(input())
    rank = {}
    for _ in range(n):
        name, raw, unused = input().split()
        rank[name[:-1]] = int(''.join([str(D[x]) for x in raw.split("-")][::-1]).ljust(10, "1"))
    print('\n'.join(sorted(rank.keys(), key=lambda x: (-rank[x], x))))
    print("==============================")
