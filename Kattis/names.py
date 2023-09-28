s = input()
print(min([sum([1 for i in range(len(a)//2)if a[i]!=a[-1-i]])for a in[s+"."*i for i in range(len(s)+1)]]))