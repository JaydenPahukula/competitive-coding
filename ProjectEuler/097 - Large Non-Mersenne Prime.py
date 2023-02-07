
def lnmp(n):
    s = "2"
    for i in range(2, n+1):
        s = str(int(s)*2)
        if len(s) > 10:
            s = s[-10:]

    return str(28433 * int(s) + 1)[-10:]

print(lnmp(7830457))