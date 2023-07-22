for _ in range(int(input())):
    n = int(input())
    p = [tuple(map(int, input().split())) for _ in range(n)]
    
    count = 0
    vertical = {}
    horizontal = {}
    diagonal1 = {}
    diagonal2 = {}

    for x, y in p:
        for val, dic in [(x, vertical), (y, horizontal), (x-y, diagonal1), (x+y, diagonal2)]:
            if val in dic:
                count += dic[val]
                dic[val] += 1
            else:
                dic[val] = 1

    print(count*2)