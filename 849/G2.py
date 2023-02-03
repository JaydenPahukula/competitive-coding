for _ in range(int(input())):
    n, c = map(int, input().split())
    inp = input().split()
    a = sorted([(int(x)+min(i+1, len(inp)-i), int(x)+i+1) for i, x in enumerate(inp)])
    mx = 0
    for i in range(len(a)):
        d = c - a[i][1]
        if d >= 0:
            b = a.copy()
            b.pop(i)
            j = 0
            score = 1
            while j < len(b) and d-b[j][0] >= 0:
                d -= b[j][0]
                j += 1
                score += 1
            if score > mx:
                mx = score
    print(mx)

    




# for _ in range(int(input())):
#     n, c = map(int, input().split())
#     inp = input().split()
#     a = sorted([(int(x)+i+1, i) for i, x in enumerate(inp)])
#     print(a)
#     if a[0][0] <= c:
#         c -= a[0][0]
#         inp[a[0][1]] = 10**10
#         for i, x in enumerate(inp):
#             print("   ", int(x), i+1, len(inp)-i)
#         a = sorted([int(x)+min(i+1, len(inp)-i) for i, x in enumerate(inp)])
#         print(a)
#         i = 0
#         score = 1
#         while i < len(a) and c-a[i] >= 0:
#             c -= a[i]
#             i += 1
#             score += 1
#         print("              ", score)
#     else:
#         print('               0')