for _ in range(int(input())):
    input()
    s = input()
    a = 0
    b = len(s)-1
    while b > a and s[a] != s[b]:
        a += 1
        b -= 1
    print(max(b-a+1, 0))