o = []
while 1:
    s1,s2 = input().split()
    if (s1,s2) == ("0","0"): break

    if len(s1)<len(s2):s1,s2=s2,s1
    count = 0
    carry = 0
    for i in range(len(s2)):
        if carry: count += 1
        result = int(s1[-1-i]) + int(s2[-1-i]) + carry
        carry = max(0,result-9)
    for i in range(len(s1)-len(s2)):
        if carry: count += 1
        result = int(s1[-1-len(s2)-i]) + carry
        carry = max(0,result-9)
    count += carry//10
    o.append(f"{count or 'No'} carry operation{'s' if count > 1 else ''}.")

print("\n".join(o))
