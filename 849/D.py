for _ in range(int(input())):
    input()
    s = input()
    mx = 0
    for i in range(1, len(s)):
        x = len(set(s[:i])) + len(set(s[i:]))
        if x > mx:
            mx = x
    print(mx)



# for _ in range(int(input())):
#     one = []
#     two = []
#     input()
#     s = input()
#     for c in s:
#         if c in two: continue
#         if c in one:
#             one.remove(c)
#             two.append(c)
#         else:
#             one.append(c)
#     print(2*len(two)+len(one))