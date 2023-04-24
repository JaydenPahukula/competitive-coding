s = input()
n = len(s)
#first layer
print("..#..", end='')
for i in range(n-1):
    if i % 3 == 1:  print(".*..", end='')
    else:           print(".#..", end='')
print()
#second layer
print(".#.#.", end='')
for i in range(n-1):
    if i % 3 == 1:  print("*.*.", end='')
    else:           print("#.#.", end='')
print()
#third layer
print(f"#.{s[0]}.#", end='')
for i in range(n-1):
    if i % 3 == 0 and i < n-2: print(f".{s[1+i]}.*", end='')
    elif i % 3 == 1:print(f".{s[1+i]}.*", end='')
    else:           print(f".{s[1+i]}.#", end='')
print()
#fourth layer
print(".#.#.", end='')
for i in range(n-1):
    if i % 3 == 1:  print("*.*.", end='')
    else:           print("#.#.", end='')
print()
#fifth layer
print("..#..", end='')
for i in range(n-1):
    if i % 3 == 1:  print(".*..", end='')
    else:           print(".#..", end='')