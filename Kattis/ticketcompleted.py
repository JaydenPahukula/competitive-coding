n, m = map(int, input().split())
pointer = [i for i in range(n)]
size = [1 for _ in range(n)]

def find(a):
    if pointer[a] == a: return a
    result = find(pointer[a])
    pointer[a] = result
    return result

total = n * (n-1) // 2
for _ in range(m):
    i, j = map(int, input().split())
    fi = find(i-1)
    fj = find(j-1)
    if fj != fi:
        total -= size[fj] * size[fi]
        size[fj] += size[fi]
        pointer[fi] = fj

print(1 - total / (n * (n-1) // 2))