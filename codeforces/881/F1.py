for _ in range(int(input())):
    for _ in range(int(input())):
        inp = input().split()
        connections = [[]]
        if inp[0] == "+":
            v, x = map(int, inp[1:])
            u = len(connections)
            connections[v-1].append((u, x))
            connections.append([(v-1, x)])
        else:
            start, end, k = map(int, inp[1:])

            q = [(start-1, -1, 0)]
            while q:
                curr, parent, total = q.pop()
                print("  ", curr)

                if curr == end-1:
                    if total == k:
                        print("YES")
                        break
                    else:
                        print("NO")

                for child, weight in connections[curr]:
                    q.append(child, curr, total+weight)
            else:
                print("NO")
