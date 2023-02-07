
fracs = []
for d in range(11, 100):
    for n in range(11, d):
        for c in str(n):
            if c == '0': continue
            if c in str(d):
                n1 = int(str(n).replace(c,'',1))
                d1 = int(str(d).replace(c,'',1))
                if d1 == 0: continue
                if n1/d1 == n/d:
                    fracs.append((n,d))

pn = 1
pd = 1
for frac in fracs:
    pn *= frac[0]
    pd *= frac[1]
print(pn, '/', pd)
