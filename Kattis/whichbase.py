for i in range(int(input())):
    s = input().split()[1]
    print(i+1, 0 if "8" in s or "9" in s else int(s, 8), int(s, 10), int(s, 16))