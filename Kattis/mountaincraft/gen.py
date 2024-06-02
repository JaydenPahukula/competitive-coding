# import random
# q = 200
# w = 10000
# print(q,w)
# mountains = [(random.randint(0,w+1),random.randint(0,w)) for _ in range(q//4)]
# for _ in range(q):
#     print(*random.choice(mountains))

import random
q = 200000
w = 1000000000
print(q,w)
mountains = [(random.randint(0,w+1),random.randint(0,1000000000)) for _ in range(q//4)]
for _ in range(q):
    print(*random.choice(mountains))
