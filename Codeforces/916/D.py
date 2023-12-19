for _ in range(int(input())):
    n = int(input())
    a = [list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))]
    b = [[],[],[]]
    for j in range(3):
        b[j] = sorted([i for i in range(n)], key=lambda x:a[j][x], reverse=True)
        a[j].sort(reverse=True)
    
    score = 0
    for i in range(3):
        for j in range(3):
            if b[0][i] == b[1][j]: continue
            for k in range(3):
                if b[0][i] == b[2][k] or b[1][j] == b[2][k]: continue
                score = max(score, a[0][i]+a[1][j]+a[2][k])
    
    print(score)