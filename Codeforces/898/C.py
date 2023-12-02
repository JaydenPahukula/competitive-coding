for _ in range(int(input())):
    points = 0
    for y in range(10):
        score1 = 6-int(abs(y-4.5)+0.5)
        line = input()
        for x in range(10):
            if line[x] == "X":
                score2 = 6-int(abs(x-4.5)+0.5)
                points += min(score1, score2)
    print(points)