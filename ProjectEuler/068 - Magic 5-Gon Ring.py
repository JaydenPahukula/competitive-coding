#wip

def printring(input):

    print(f"\n\n     ({input[0]})")
    print("       \ ")
    print(f"       ({input[1]})")
    print("       / \ ")
    print(f"     ({input[5]})--({input[3]})---({input[2]})")
    print("     /")
    print(f"   ({input[4]})")
    
    

    return


def solution():

    outsideRing = [0] * 3
    insideRing = [0] * 3
    count = 0

    for a in range(1, 7):
        for b in [x for x in range(1, 7) if x != a]:
            for c in [x for x in range(1, 7) if x != a and x != b]:
                total = a + b + c
                for d in range(a+1, 7):
                    e = total - c - d
                    if e not in range(1, 7):
                        break
                    f = total - e - b
                    if f not in range(1, 7):
                        break
                    if d == b or f == c or a == e or a == d or d == f:
                        pass
                        #break
                    s = f'{a},{b},{c}; {d},{c},{e}; {f},{e},{b}'
                    if b == c or c == e or e == b:
                        break
                    line1 = [a, b, c]
                    line2 = [d, c, e]
                    line3 = [f, e, b]
                    if len([*set(line1)]) != 3 or len([*set(line2)]) != 3 or len([*set(line3)]) != 3:
                        break
                    if sorted(line1) == sorted(line2) or sorted(line1) == sorted(line3) or sorted(line3) == sorted(line2):
                        break
                    printring([a, b, d, c, f, e])
                    print(total)
                    count += 1


    return count

print(solution())