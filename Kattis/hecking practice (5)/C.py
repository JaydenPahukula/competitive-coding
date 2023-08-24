nonums = {"a","b","c","d","e","f","g","h","i","j","k","l","n","o","p","q","r","s","t","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"," "}
x = {"u":"1", "m":"0"}
ums = ""
for word in input().split():
    for c in word:
        if c in nonums:
            break
    else:
        ums += "".join([x[c] for c in word if c in x])
output = ""
for i in range(0, len(ums), 7):
    output += chr(int(ums[i:i+7], base=2))
print(output)