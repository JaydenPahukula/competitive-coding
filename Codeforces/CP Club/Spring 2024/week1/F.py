n = int(input())
a = list(map(int, input().split()))

if n == 1 or (n == 2 and a[0] == a[1]):
    print(-1)
else:
    if a[0] != sum(a[1:]):
        print(1)
        print(a[0])
    else:
        print(1)
        print(a[1])



# if n == 1 or (n == 2 and a[0] == a[1]):
#     print(-1)
# else:
#     for i in range(n):
#         if a[i] != sum(a[:i])+sum(a[i+1:]):
#             print(1)
#             print(a[i])
#             break
#     else:
#         print(-1)



# def r(x):
#     if len(x) == n:
#         x1 = [a[i] for i in range(n) if x[i]]
#         x2 = [a[i] for i in range(n) if not x[i]]
#         if x1 and x2 and sum(x1) != sum(x2):
#             print(len(x1))
#             print(" ".join(map(str, x1)))
#             exit()
#     else:
#         r(x+[True])
#         r(x+[False])

# r([])
# print(-1)
