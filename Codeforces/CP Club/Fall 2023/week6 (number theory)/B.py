for _ in range(int(input())):
    n = int(input())
    count = 0
    for digit in "123456789":
        s = digit
        while int(s) <= n:
            count += 1
            s += digit
    print(count)