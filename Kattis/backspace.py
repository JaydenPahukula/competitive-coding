o=[]
for c in input():
 if c=="<":o.pop()
 else:o.append(c)
print("".join(o))