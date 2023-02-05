N, M, Q = map(int, input().split())

cities = {}
for city in range(1, N+1):
    cities[city] = []
for _ in range(M):
    u, v, t = map(int, input().split())
    cities[u].append((t, v))
    cities[v].append((t, u))

print(cities)

q = [(-1, 1, -1)]
visited = []
while len(q) > 0:
    (toll, city, camefrom), *q = q
    if city in visited:
        if (t, camefrom) in cities[city]:
            cities[city].remove((t, camefrom))
        continue
    visited.append(city)
    for toll, destination in cities[city]:
        q.append((toll, destination, city))
    q.sort()

print(cities)

queries = {}
for _ in range(Q):
    a, b = map(int, input().split())
    if a in queries:
        queries[a].append(b)
    else:
        queries[a] = [b]

print()

for a in queries.keys():
    q = [(0, a)]
    mins = [-1 for _ in range(N+1)]
    visited = []
    while len(q) > 0:
        (maxtoll, city), *q = q

        visited.append(city)
        mins[city] = maxtoll

        for toll, destination in cities[city]:
            if destination not in visited:
                q.append((max(toll, maxtoll), destination))

    print(a, mins)
    for b in queries[a]:
        print(mins[b], sum([1 if x <= mins[b] else 0 for x in mins]))