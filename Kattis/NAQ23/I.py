import sys
input = sys.stdin.readline


def numDigits(n:int):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

def missing(lo:int, s:str):
    possible = []
    num = lo
    i = 0
    while i < len(s):
        if num > 99999: return []
        d = numDigits(num)
        if int(s[i:i+d]) != num:
            if possible == []: possible = [num]
            else: return []
        else:
            i += d
        num += 1
    if possible == []:
        if lo > 1: possible.append(lo-1)
        if num <= 99999: possible.append(num)
    return possible

final = []
for _ in range(int(input())):
    s = input().strip()
    out = {-1}
    for i in range(1, min(len(s),6)):
        lo = int(s[:i])
        if lo > 99998: continue
        result = missing(lo, s)
        for num in result: out.add(num)
    if int(s) >= 1 and int(s) < 99999: out.add(int(s)+1)
    if int(s) > 1 and int(s) <= 99999: out.add(int(s)-1)

    out.remove(-1)
    final.append(str(len(out)))
    final.append(" ".join(map(str, sorted(list(out)))))
print("\n".join(final))