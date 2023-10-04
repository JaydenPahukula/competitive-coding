# from math import log10

# def check(s:str, n:int):
#     if len(s) == 0: return (True, [[]])
#     for option in (n+1,n+2):
#         numDigits = int(log10(option))+1
#         if numDigits <= len(s) and int(s[:numDigits]) == option:
#             result, l = check(s[numDigits:], option)
#             if result: return (True, [[option]+x for x in l])
#             else: return (False, [[]])
#     return (False, [[]])

# for _ in range(int(input())):
#     s = input()
#     out = []
#     for i in range(1,len(s)//2+2):
#         option = int(s[:i])
#         result, l = check(s[i:], option)
#         for seq in [[option]+x for x in l]:
#             lo,hi = seq[0],seq[-1]
#             if hi-lo == len(seq):
#                 out.append([x for x in range(lo, hi+1) if x not in seq][0])
#     print(len(out))
#     print(" ".join(map(str, out)))

def missing(lo:int, s:str):
    possible = []
    num = lo
    while s:
        if num > 99999: return []
        snum = str(num)
        if s[:len(snum)] != snum:
            if len(possible) == 0: possible = [num]
            else: return []
        else:
            s = s[len(snum):]
        num += 1
    if possible == []:
        if lo > 1: possible.append(lo-1)
        if num <= 99999: possible.append(num)
    return possible

for _ in range(int(input())):
    s = input()
    out = {-1}
    for i in range(1, min(len(s),6)):
        lo = int(s[:i])
        if lo > 99998: continue
        result = missing(lo, s)
        for num in result: out.add(num)
    if int(s) >= 1 and int(s) < 99999: out.add(int(s)+1)
    if int(s) > 1 and int(s) <= 99999: out.add(int(s)-1)

    out.remove(-1)
    print(len(out))
    print(" ".join(map(str, sorted(list(out)))))