for _ in range(int(input())):
    n = int(input())
    s1 = input()
    s2 = input()
    s3 = input()
    t = "_"*n
    for i in range(n):
        if s1[i] == s2[i]:
            t[i] == s1[i]

    for i in range(n):
        if t[i] == "_":
            if s3[i] != s2[i] and s3[i] != s1[i]: break
        else:
            if t[i] != s3[i]: break
    else:
        print("NO")
        continue
    print("YES")
