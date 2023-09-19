n = int(input())
s = input()

order = [str(x) for x in range(1, n+1)]
i = 0
while i < n-1:
    count = 0
    while i+count < n-1 and s[i+count] == "L":
        count += 1
    order[i:i+count+1] = order[i:i+count+1][::-1]
    i += count+1
print("\n".join(order))