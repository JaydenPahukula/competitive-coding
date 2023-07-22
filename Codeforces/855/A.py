def isMeow(s:str):
    i = 0
    check = ["Mm", "Ee", "Oo", "Ww", ""]
    for c in s:
        if c not in check[i]:
            if c not in check[i+1]:
                return False
            i += 1
    return i == 3

for _ in range(int(input())):
    n = int(input())
    if isMeow(input()): print("YES")
    else: print("NO")
