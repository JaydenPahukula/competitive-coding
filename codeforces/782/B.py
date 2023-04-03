import sys
sys.setrecursionlimit(2000)

n = int(input())
location = list(map(int, input().split()))
speed = list(map(int, input().split()))

def timeToMeet(meetingSpot:float):
    times = [0 for _ in range(n)]
    for i in range(n):
        times[i] = abs(location[i]-meetingSpot) / speed[i]
    return max(times)

def ternarySearch(start, end):
    mid1 = start + (end-start)/3
    mid2 = end - (end-start)/3
    tmid1 = timeToMeet(mid1)
    tmid2 = timeToMeet(mid2)
    if abs(mid1-mid2) < 0.000001:
        return tmid1
    elif tmid1 < tmid2:
        return ternarySearch(0, mid2)
    else:
        return ternarySearch(mid1, end)
    
print(ternarySearch(min(location), max(location)))
