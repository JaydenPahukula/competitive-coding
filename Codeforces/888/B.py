for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    mask = [x%2 for x in l]
    sortedMask = [x%2 for x in sorted(l)]
    if mask == sortedMask:
        print("YES")
    else:
        print("NO")