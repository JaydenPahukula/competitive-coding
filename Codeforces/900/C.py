def sumUpTo(n:int): return (n*(n+1))//2
for _ in range(int(input())):
    n, k, target = map(int, input().split())
    highest = sumUpTo(n)-sumUpTo(n-k)
    lowest = sumUpTo(k)
    if target > highest or target < lowest: print("NO")
    else: print("YES")