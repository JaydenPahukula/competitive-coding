for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    right = [0]*n
    for i in range(1,n):
        right[i] = right[i-1]
        if i == 1 or a[i]-a[i-1] < a[i-1]-a[i-2]:
            right[i] += 1
        else:
            right[i] += a[i]-a[i-1]
    
    left = [0]*n
    for i in range(n-2,-1,-1):
        left[i] = left[i+1]
        if i == n-2 or a[i+1]-a[i] < a[i+2]-a[i+1]:
            left[i] += 1
        else:
            left[i] += a[i+1]-a[i]

    for _ in range(int(input())):
        start, end = map(int, input().split())
        if start < end: # right
            print(right[end-1]-right[start-1])
        else: # left
            print(left[end-1]-left[start-1])