for _ in range(int(input())):
    n = int(input())
    s = input()
    a = ""
    lookingfor = ''
    for c in s:
        if lookingfor == '':
            lookingfor = c
        elif lookingfor == c:
            lookingfor = ''
            a += c
    print(a)