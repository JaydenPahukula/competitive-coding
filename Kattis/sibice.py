n,w,h=map(int,input().split())
for _ in "_"*n:print(("DA","NE")[int(input())>abs(w+1j*h)])


# n, w, h = map(int, input().split())
# for _ in range(n):
#     if int(input()) <= ((w**2)+(h**2))**(0.5): print("DA")
#     else: print("NE")