t = int(input())
for _ in range(t):
    encodedmessage = input()
    decodedmessage = ""
    size = int(len(encodedmessage)**(1/2))
    for y in range(size-1, -1, -1):
        for x in range(size):
            decodedmessage += encodedmessage[x*size + y]
    print(decodedmessage)