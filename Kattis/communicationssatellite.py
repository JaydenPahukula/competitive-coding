import heapq

def getDistance(s1, s2):
    return ((s1[0]-s2[0])**2+(s1[1]-s2[1])**2)**(1/2) - s1[2] - s2[2]

N = int(input())
satellites = []
for _ in range(N):
    satellites.append(tuple(map(int, input().split())))

connected = set()
total = 0
q = []
heapq.heappush(q, (0, satellites[0]))
while len(connected) < N:
    distance, satellite = heapq.heappop(q)

    if satellite in connected: continue
    connected.add(satellite)

    total += distance

    for newSatellite in satellites:
        if newSatellite not in connected:
            heapq.heappush(q, (getDistance(satellite, newSatellite), newSatellite))

print(total)