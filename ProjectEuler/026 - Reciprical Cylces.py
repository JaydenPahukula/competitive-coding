
import mpmath as mp

l = 0
dl = 0
DEBUG = False




mp.mp.dps = 10000

for d in range(2,1000):
    string = str(mp.mpf(1)/mp.mpf(d))
#    if len(string) >= 202:
#        string = string[:-1]
    if DEBUG: 
        print("\n\n------------------------\nd = " + str(d) + "\n1/d = " + string[:-1])
    for i in range(2, len(string)):
        if DEBUG:
            print("searching for patterns in " + string[i:-1])
        num = string[i]
        success = False
        pattern = num
        for j in range(i+1,len(string)):
            if pattern[0] == string[j]:
                if DEBUG:
                    print("found pattern (" + pattern + "):  verifying...")
                if len(string) - j < len(pattern):
                    if DEBUG:
                        print("pattern too long, couldn't verify")
                    break
                fail = False
                for k in range(len(string)-j-1):
                    #print("   comparing " + string[k+j] + " and " + pattern[k % len(pattern)])
                    if string[k+j] != pattern[k % len(pattern)]:
                        if DEBUG:
                            print("failed")
                        fail = True
                        break
                if fail == False:
                    if DEBUG:
                        print("verified!!!")
                    success = True
                    break
            pattern += string[j]
            
        if success:
            if DEBUG:
                print("\npattern = " + pattern)
            if len(pattern) > l:
                if DEBUG:
                    print("new longest pattern! l = " + str(len(pattern)))
                l = len(pattern)
                dl = d
            break
        else:
            if DEBUG:
                print("didnt find pattern")
            pattern = ""
print("\n\n\n\nlongest pattern is at d = " + str(dl) + " with l = " + str(l))
