for _ in range(int(input())):
    n = int(input())
    rules = []
    a = []
    for i in range(n):
        a = ([int(x) for x in input().split()])
        for j in range(n-2):
            rule = (a[j], a[j+1])
            if rule not in rules:
                rules.append(rule)

    final = []
    for i in range(n):
        nextDigit = [True if i+1 not in final else False for i in range(n)]
        for num in nextDigit:
            if num+1 in final:
                nextDigit[num] = False
        for x, y in rules:
            if nextDigit[y-1]:
                nextDigit[y-1] = False
        final.append(nextDigit.index(True)+1)
        toRemove = []
        for x, y in rules:
            if x == final[-1]:
                toRemove.append((x, y))
        for rule in toRemove:
            rules.remove(rule)
    for num in final:
        print(num, end=' ')
    print()

    
        

