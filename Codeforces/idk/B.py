for _ in range(int(input())):
    n = int(input())
    out = []
    if n%2:
        for i in range(0, n-3, 2):
            out.append(str(i+2))
            out.append(str(i+1))
        out.append(str(n))
        out.append(str(n-2))
        out.append(str(n-1))
    else:
        for i in range(0, n, 2):
            out.append(str(i+2))
            out.append(str(i+1))
    print(" ".join(out))