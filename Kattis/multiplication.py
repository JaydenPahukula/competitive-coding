while 1:
    a,b = input().split()
    if (a,b) == ("0","0"): break
    na,nb = len(a),len(b)
    la,lb = list(map(int,list(a))),list(map(int,list(b)))
    table = [[tuple(str(la[x]*lb[y]).rjust(2,"0")) for x in range(na)] for y in range(nb)]
    ans = tuple(str(int(a)*int(b)).rjust(na+nb," "))
    
    print("+--"+("----"*na)+"-+")
    print("|  "+"".join(f" {digit}  " for digit in la)+" |")
    print("| +"+("---+"*na)+" |")
    for y in range(nb):
        print(f"|{'/' if y and ans[y-1] != ' ' else ' '}|"+"".join(f"{table[y][x][0]} /|" for x in range(na))+" |")
        print("| |"+(" / |"*na)+f"{lb[y]}|")
        print(f"|{ans[y]}|"+"".join(f"/ {table[y][x][1]}|" for x in range(na))+" |")
        print("| +"+("---+"*na)+" |")
    print(f"|"+"".join(("/" if ans[nb+x-1] != " " else " ")+f" {ans[nb+x]} " for x in range(na))+"   |")
    print("+--"+("----"*na)+"-+")
