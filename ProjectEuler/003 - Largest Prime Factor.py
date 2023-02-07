NUM = 600851475143
i = 1
fail = False
while 1:
    i += 1
    #if factor
    if NUM % i == 0:
        print("testing factor:",round(NUM/i))
        #if corresponding factor is prime
        for n in range(1,round(NUM/i)-1):
            n += 1
            if (NUM/i) % n == 0:
                fail = True
                print("failed")
                break
        if fail == False:
            print("WINNER! -",round(NUM/i))
            quit()
        fail = False
