import math

for a in range(1,1001):
    for b in range(1,1001):
        c = math.sqrt(a**2+b**2)
        if c % 1 == 0:
            print("found pythagorean triplet - ",a,b,int(c))
            print("sum =",a+b+int(c))
            if a+b+int(c) == 1000:
                print("winner!\nproduct =",a*b*int(c))
                quit()