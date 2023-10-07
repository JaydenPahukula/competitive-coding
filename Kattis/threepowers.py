while 1:
    n = int(input())
    if n == 0: break

    b = [c=="1" for c in bin(n-1)[2:]][::-1]
    print("{"+",".join([" "+str(3**i) for i in range(len(b)) if b[i]])+" }")