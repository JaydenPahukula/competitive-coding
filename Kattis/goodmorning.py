def check(s:str):
    for i in range(len(s)-1):
        if s[i] == "0" and s[i+1] not in {"0"}: return False
        if s[i] == "1" and s[i+1] not in {"1","2","3","4","5","6","7","8","9","0"}: return False
        if s[i] == "2" and s[i+1] not in {"2","3","5","6","8","9","0"}: return False
        if s[i] == "3" and s[i+1] not in {"3","6","9"}: return False
        if s[i] == "4" and s[i+1] not in {"4","5","6","7","8","9","0"}: return False
        if s[i] == "5" and s[i+1] not in {"5","6","8","9","0"}: return False
        if s[i] == "6" and s[i+1] not in {"6","9"}: return False
        if s[i] == "7" and s[i+1] not in {"7","8","9","0"}: return False
        if s[i] == "8" and s[i+1] not in {"8","9","0"}: return False
        if s[i] == "9" and s[i+1] not in {"9"}: return False
    return True
isValid = [check(str(n)) for n in range(201)]

for _ in range(int(input())):
    n = int(input())
    for d in range(201):
        if isValid[n+d]:
            print(n+d)
            break
        if isValid[n-d]:
            print(n-d)
            break