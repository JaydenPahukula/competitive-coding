for _ in range(int(input())):
    n = int(input())
    evensum = 0
    oddsum = 0
    for num in map(int, input().split()):
        if num % 2 == 0:
            evensum += num
        else:
            oddsum += num
    if evensum > oddsum:
        print("YES")
    else:
        print("NO")
    