for _ in range(int(input())):
    p1 = tuple(map(int, input().split()))
    p2 = tuple(map(int, input().split()))
    p3 = tuple(map(int, input().split()))
    p4 = tuple(map(int, input().split()))
    p1,p2,p3,p4 = sorted([p1,p2,p3,p4])
    print((p3[0]-p1[0])*(p2[1]-p1[1]))