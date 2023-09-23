first = 0
for _ in range(int(input())):
    n = int(input())
    if first == 0:
        first = n
    elif n%first == 0:
        print(n)
        first = 0
