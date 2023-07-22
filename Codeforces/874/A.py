for _ in range(int(input())):
    n = int(input())
    s = input()
    melodies = set()
    for i in range(n-1):
        melodies.add(s[i:i+2])
    print(len(melodies))