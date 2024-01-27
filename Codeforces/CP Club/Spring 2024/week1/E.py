for _ in range(int(input())):
    s = input()
    n = len(s)
    o = set()
    if n == 1:
        print(s)
    else:
        s = s+"_"
        i = 0
        while i < n:
            if s[i] != s[i+1]: o.add(s[i])
            else: i += 1
            i += 1
        print("".join(sorted(o)))