for _ in range(int(input())):
    n = int(input())
    a = [bool(int(x)) for x in input().split()]
    maxStreak = 0
    streak = 0
    for x in a:
        if not x:
            streak += 1
            if streak > maxStreak:
                maxStreak = streak
        else:
            streak = 0
    print(maxStreak)