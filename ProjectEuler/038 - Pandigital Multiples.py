

def pandigital(s:str):
    if '0' in s or len(s) > 9:
        return 1
    l = []
    for c in s:
        if c in l:
            return 1
        l.append(c)
    if len(l) == 9:
        return 0
    return -1
#  1 - fail/over
#  0 - success
# -1 - under

def highestPandigitalMultiple():
    maxs = 0
    for num in range(10000):
        s = ""
        n = 1
        while 1:
            s += str(num * n)
            x = pandigital(s)
            if x == -1:
                n += 1
            if x == 0:
                if int(s) > maxs:
                    maxs = int(s)
            if x == 1:
                break
    return maxs


print(highestPandigitalMultiple())