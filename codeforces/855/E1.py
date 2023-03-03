def canChange(s:str, t:str):
    s = list(s)
    t = list(t)
    n = len(s)
    for i in range(n):
        print(" ", s, t)
        if s[i] != t[i]:
            if i < n-3 and s[i+3] == t[i]:
                s[i], s[i+3] = s[i+3], s[i]
            elif i < n-4 and s[i+4] == t[i]:
                s[i], s[i+4] = s[i+4], s[i]
            else:
                return False
    print(" ", s, t)
    return True

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    t = input()
    if canChange(s, t): print("YES")
    else: print("NO")