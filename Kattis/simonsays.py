for _ in range(int(input())):
    s = input()
    if len(s)>11 and s[:11]=="Simon says ":print(s[11:])