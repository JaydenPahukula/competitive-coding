n = int(input())
prices = sorted([int(input().split()[1]) for _ in range(n)], reverse=True)
print(sum([prices[i] for i in range(0,n,2)]))