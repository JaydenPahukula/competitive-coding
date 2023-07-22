for _ in range(int(input())):
    l = [(i,) + tuple(map(int, input().split())) for i in range(int(input()))]
    print(sorted(l, key=lambda x: (x[1] > 10, -x[2]))[0][0]+1)