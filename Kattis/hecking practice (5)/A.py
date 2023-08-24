for _ in range(int(input())):
    s = input()
    for i in range(1, len(s)):
        if s[i] == s[0]:
            pattern = s[0:i]
            for j in range(i, len(s)):
                if s[j] != pattern[j%len(pattern)]:
                    break
            else:
                print(len(pattern))
                break
    else:
        print(len(s))