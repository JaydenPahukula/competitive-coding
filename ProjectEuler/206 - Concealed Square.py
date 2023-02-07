
def check(n:int):
    s = str(n)
    if len(s) != 19:
        return False
    if s[0] != '1' or s[2] != '2' or s[4] != '3' or s[6] != '4' or s[8] != '5' or s[10] != '6' or s[12] != '7' or s[14] != '8' or s[16] != '9' or s[18] != '0':
        return False
    return True

def solution():
    n = 1_010_101_010
    while 1:
        if check(n**2):
            return n
        n += 10
    return "idk"

print(solution())