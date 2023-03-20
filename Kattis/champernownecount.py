n, k = map(int, input().split())
num = 0
count = 0
for i in range(1, n+1):
    num = int(str(num)+str(i)) % k
    if num == 0: count += 1
print(count)