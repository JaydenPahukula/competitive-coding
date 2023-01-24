t = int(input())
for _ in range(t):
    n = int(input())
    x = [int(num) for num in input().split(' ')]
    print(2*(max(x)-min(x)))