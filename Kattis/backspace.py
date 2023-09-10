# o=[]
# [o.pop()if c=="<"else o.append(c)for c in input()]
# print("".join(o))
o=["\b"if c=="<"else c for c in input()]
print("".join(o)+" ")