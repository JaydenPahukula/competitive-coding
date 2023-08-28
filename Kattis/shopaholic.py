n = int(input())
l = sorted(map(int, input().split()))
print(sum([l[i] for i in range(n-3, -1, -3)]))