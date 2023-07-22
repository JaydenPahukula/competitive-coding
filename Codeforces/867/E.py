for _ in range(int(input())):
    n = int(input())
    s = input()
    if n % 2 == 1:
        print(-1)
        continue
    h = n//2
    swaps = 0
    for i in range(h):
        if s[i] == s[-1-i]:
            #swap
            pass