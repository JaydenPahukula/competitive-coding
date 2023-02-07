
def divisors(n:int):
    divisors = [1]
    for i in range(2, round(n/2+1)):
        if n % i == 0:
            divisors.append(i)
    return divisors

#takes forever but the answer shows up after about 2 seconds
def amicableChains(N:int):
    bigList = [1] * N
    longest = 0
    maxChain = []
    for i in range(1, N):

        #dont check duplicates
        if bigList[i] == 1:

            #build the chain starting with i
            chain = [i]
            while 1:

                #break if chain ends (prime)
                divs = divisors(chain[-1])
                if divs == [1]:
                    break

                next = sum(divs)
                
                #break if chain exceeds N
                if next >= N:
                    break

                #success
                if next in chain:
                    #only take the part that loops
                    while chain[0] != next:
                        chain.pop(0)
                    print(chain)
                    #check if longest
                    if len(chain) > longest:
                        longest = len(chain)
                        maxChain = chain
                    break

                #break if already found
                if bigList[next] == 0:
                    break

                bigList[next] = 0
                chain.append(next)
        
    return min(maxChain)

print(amicableChains(1000000))