S = "codeforces"
for _ in range(int(input())):
    s = input()
    count = 0
    for i in range(10):
        if S[i] != s[i]: count += 1
    print(count)