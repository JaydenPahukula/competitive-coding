from collections import deque

for _ in range(int(input())):
    l = [input() for _ in range(int(input()))]
    s = set()
    d = deque()
    mx = 0
    for snowflake in l:
        while snowflake in s:
            s.remove(d.popleft())
        d.append(snowflake)
        s.add(snowflake)
        mx = max(mx, len(s))
    print(mx)
