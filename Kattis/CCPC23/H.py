# n, f = map(int, input().split())
# grid = [[0 for _ in range(n)] for _ in range(n)]
# for y in range(n):
#     grid[y] = list(map(int, input().split()))
n = 7
starty = 3
startx = 3
fuel = 2
for y in range(max(starty-fuel, 0), min(starty+fuel+1, n)):
    print(y, "-----")
    for x in set([startx+fuel-abs(y-starty), startx-fuel+abs(y-starty)]):
        print(y, x)

# maxScore = 0
# for starty in range(n):
#     for startx in range(n):
#         if starty != 0 and startx != 0 and starty != n-1 and startx != n-1:
#             continue

#         fuel = f
#         for y in range(max(starty-fuel, 0), min(starty+fuel), n-1):
#             for x in [startx+fuel-abs(y-starty), startx-fuel+abs(y-starty)]:
                

# print(maxScore)