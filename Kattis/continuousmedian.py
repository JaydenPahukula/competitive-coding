import statistics

T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(num) for num in input().split(' ')]
    total = 0
    a = []
    for i in range(N):
        a.append(A[i])
        total += int(statistics.median(a))
        #total += (a[i//2] + a[-(-i//2)]) // 2
    print(total)