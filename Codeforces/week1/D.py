for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a==b+c or b==a+c or c==a+b or (a==b and not c%2) or (b==c and not a%2) or (c==a and not b%2): print("YES")
    else: print("NO")