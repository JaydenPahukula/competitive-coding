for _ in range(int(input())):
    n = int(input())
    s = input()
    i = 0
    while s[i] == "W": i += 1
    j = n-1
    while s[j] == "W": j -= 1
    print(j-i+1)