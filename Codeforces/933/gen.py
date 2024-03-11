from random import randint

h = randint(0,1000)
w = (2*10**5)//h
k = randint(1,h)
d = randint(1,w-1)

print(1)
print(h,w,k,d)
for _ in range(h):
    print(0,*[randint(0,10**6) for _ in range(w-2)],0)
