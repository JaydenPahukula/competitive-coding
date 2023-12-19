for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    c = sorted([i for i in range(n)], key=lambda x:a[x]+b[x], reverse=True)
    score = 0
    for i in range(n):
        move = c[i]
        if i % 2 == 0:
            score += a[move]-1
        else:
            score -= b[move]-1
    
    print(score)