
def chain(n):
    x = n
    i = 1
    while 1:
        if x == 1: #if 1
            return i #done
        if x % 2 == 0: #if even
            x /= 2
        else: #if odd
            x *= 3
            x += 1
        x = round(x) #round x
        i += 1 #step i

def longestCollatzSequence(n):
    longest = 0
    longesti = 0
    for i in range(1,n+1):
        x = chain(i)
        if x >= longest:
            longest = x
            longesti = i
        
    return longesti


print(longestCollatzSequence(1000000))