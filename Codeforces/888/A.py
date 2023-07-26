for _ in range(int(input())):
    n, m, k, h = map(int, input().split())
    l = list(map(int, input().split()))
    count = 0
    for person in l:
        diff = abs(h-person)
        if diff != 0 and diff <= (m-1)*k and diff % k == 0:
            count += 1
    print(count)