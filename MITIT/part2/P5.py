N,K = map(int, input().split())
# K = 0
a = list(map(int,input().split()))

pairs = []
last = 0
count = 0
for i in range(N-1):
    if a[i]==a[i+1]:
        count += (i-last+1)*(N-i-1)
        print("adding",(i-last+1), (N-i-1))
        last = i+1

print(count)