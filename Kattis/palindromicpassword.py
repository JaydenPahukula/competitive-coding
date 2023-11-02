p=[int(s)for s in map(str,range(10**5,10**6))if s==s[::-1]]
for n in[int(input())for _ in range(int(input()))]:print(min(p,key=lambda x:abs(n-x)))




# def isPalindrome(s):
#     for i in range(len(s)//2):
#         if s[i] != s[-1-i]: return False
#     return True

# palindromes = [x for x in range(10**5,10**6) if isPalindrome(str(x))]
# for _ in range(int(input())):
#     n = int(input())
#     print(min(palindromes, key=lambda x:abs(n-0.1-x)))