# from math import factorial
# n = int(input())
# hi = 205022
# lo = 1
# while hi > lo+1:
#     mid = (hi+lo)//2
#     if factorial(mid) <= n:
#         lo = mid
#     else:
#         hi = mid
# print(lo)

from math import lgamma
n = 1
for i in range(2,205023):
    n *= i
    print(i, lgamma(n+1))
# print(i, len(str(n)))