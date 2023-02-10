a,b,c = map(int, input().split(" "))

outcomes = []

outcomes.append((a+b)+c)
outcomes.append((a-b)+c)
outcomes.append((a*b)+c)
if a % b == 0:
    outcomes.append((a/b)+c)
outcomes.append((a+b)-c)
outcomes.append((a-b)-c)
outcomes.append((a*b)-c)
if a % b == 0:
    outcomes.append((a/b)-c)
outcomes.append((a+b)*c)
outcomes.append((a-b)*c)
outcomes.append((a*b)*c)
if a % b == 0:
    outcomes.append((a/b)*c)
if (a+b) % c == 0:
    outcomes.append((a+b)/c)
if (a-b) % c == 0:
    outcomes.append((a-b)/c)
if (a*b) % c == 0:
    outcomes.append((a*b)/c)
if a % b == 0 and (a/b) % c == 0:
    outcomes.append((a/b)/c)

outcomes.sort()

for i in outcomes:
    if i >= 0:
        print(int(i))
        break