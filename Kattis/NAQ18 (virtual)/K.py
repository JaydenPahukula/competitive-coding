task, s = input().split()
if task == "E":
    output = []
    i = 0
    while i < len(s):
        output.append(s[i])
        count = 1
        while i < len(s)-1 and s[i+1] == s[i]:
            i += 1
            count += 1
        output.append(str(count))
        i += 1
    print("".join(output))
else:
    for i in range(0,len(s),2):
        print(s[i]*int(s[i+1]), end="")
    print()