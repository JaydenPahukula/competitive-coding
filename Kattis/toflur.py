n = int(input())
a = sorted(map(int, input().split()))
print(sum([(a[i]-a[i+1])**2 for i in range(n-1)]))