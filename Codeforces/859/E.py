import sys

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    acum = a.copy()
    for i in range(1, n):
        acum[i] += acum[i-1]
    top = n
    bottom = 0
    while 1:
        k = int((top+bottom)/2)
        if k == 1:
            print("!", k)
            sys.stdout.flush()
            break
        print("?", k-bottom, " ".join([str(num) for num in range(bottom+1, k+1)]))
        sys.stdout.flush()
        if int(input()) > acum[k-1]:
            top = k
        else:
            bottom = k
