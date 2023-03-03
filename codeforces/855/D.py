for _ in range(int(input())):
    n = int(input())
    s = input()
    count = n-1
    for i in range(n-2):
        if s[i] == s[i+2]:
            count -= 1
    print(count)