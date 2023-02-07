for _ in range(int(input())):
    x = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    sets = []
    for num in a:
        for i in range(len(sets)):
            if num == sets[i]:
                sets[i] = num+1
                break
        else:
            sets.append(num+1)
    print(len(sets))