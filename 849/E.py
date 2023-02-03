for _ in range(int(input())):
    input()
    data = input()
    negCount = data.count('-')
    a = [abs(int(x)) for x in data.split()]
    if negCount % 2 == 0:
        print(sum(a))
    else:
        a.sort()
        print(sum(a[1:])-a[0])