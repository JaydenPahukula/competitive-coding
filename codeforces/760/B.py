for _ in range(int(input())):
    n = int(input())
    bigrams = list(input().split())
    found = False
    last = bigrams[0][0]
    print(bigrams[0][0], end='')
    for i in range(n-2):
        if not found and bigrams[i][0] != last:
            print(bigrams[i][0], end='')
            found = True
        print(bigrams[i][1], end='')
        last = bigrams[i][1]
    if not found:
        print('a', end='')
    print()