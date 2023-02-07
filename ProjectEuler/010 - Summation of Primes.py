def sumOfPrimes(n):
    sum = 0
    nums = [True] * n
    for i in range(2, n):
        if nums[i]:
            sum += i
            for j in range(i*i,n,i):
                nums[j] = False
    return sum
    
print(sumOfPrimes(2000000))