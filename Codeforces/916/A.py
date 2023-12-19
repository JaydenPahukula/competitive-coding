for _ in range(int(input())):
    n = int(input())
    s = input()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    total = 0
    for i in range(26):
        if s.count(alphabet[i]) >= i+1:
            total += 1
    print(total)