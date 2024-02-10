n = int(input())
b = list(map(int, input().split()))
total = b[0] + b[-1]
for i in range(1,n-1):
    total += min(b[i-1],b[i])
print(total)