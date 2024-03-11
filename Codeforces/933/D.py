import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n,m,x = map(int,input().split())
    players = [False for _ in range(n)]
    players[x-1] = True
    for _ in range(m):
        newPlayers = [False for _ in range(n)]
        distance,direction = input().split()
        if direction in "0?":
            for i in range(n):
                if players[i]: newPlayers[(i+int(distance))%n] = True
        if direction in "1?":
            for i in range(n):
                if players[i]: newPlayers[(i-int(distance))%n] = True
        players = newPlayers
    print(sum(players))
    print(" ".join(str(i+1) for i in range(n) if players[i]))
