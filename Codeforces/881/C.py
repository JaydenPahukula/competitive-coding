for _ in range(int(input())):
    n = int(input())
    total = 1
    while n > 1:
        total += n
        n = n//2
    print(total)