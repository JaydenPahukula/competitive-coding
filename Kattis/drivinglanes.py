n, m = map(int, input().split())
k, r = map(int, input().split())
straights = [int(input()) for _ in range(n)]
curves = [tuple(map(int, input().split())) for _ in range(n-1)]

# only keep track of best distance for each lane
lanes = [0 for _ in range(m)]

if n > 1:
    # first straightaway
    for lane in range(m):
        if lane*k <= straights[0]:
            lanes[lane] = straights[0] + lane*r
        else:
            lanes[lane] = (10**12)

    # first curve
    for lane in range(m):
        s, c = curves[0]
        lanes[lane] += s + (c * (lane+1))

    # middle stuff
    for i in range(1, n-1):
        numLaneChanges = straights[i]//k
        for lane in range(m):
            # change lanes
            options = [lanes[x]+straights[i]+(r*abs(lane-x)) for x in range(max(lane-numLaneChanges, 0), min(lane+numLaneChanges+1, m))]
            lanes[lane] = min(options)
            # curve
            s, c = curves[i]
            lanes[lane] += s + (c * (lane+1))

# last straightaway
for lane in range(m):
    if lane*k <= straights[-1]:
        lanes[lane] += straights[-1] + lane*r
    else:
        lanes[lane] += (10**12)
print(min(lanes))