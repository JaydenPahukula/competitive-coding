alphabet = "abcdefghijklmnopqrstuvwxyz"
for _ in range(int(input())):
    n = int(input())
    trace = list(map(int, input().split()))
    letterCounts = {letter:0 for letter in alphabet}
    s = []
    for i in range(n):
        x = trace[i]
        for letter in letterCounts:
            if letterCounts[letter] == x:
                s.append(letter)
                letterCounts[letter] += 1
                break
    print("".join(s))
