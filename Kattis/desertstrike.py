from math import ceil, floor

K, W = map(int, input().split())
WK = W//K

totalArea = 0

pieceArea = 2*ceil(K/2)+floor(K/2)
totalArea += pieceArea * WK

fillArea = 2*K
totalArea += fillArea * ((WK)*(WK-1))//2

h = 2 * WK
if h != floor(W*2/K):
    h += 1
    totalArea += WK*K + ceil(K/2)

totalArea *= 4

totalArea += (W-h)**2

print(totalArea)