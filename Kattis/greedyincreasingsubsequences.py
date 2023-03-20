n = int(input())
sequences = []
for num in map(int, input().split()):
    if sequences != [] and num < sequences[-1][-1]:
        sequences.append([num])
    else:
        for sequence in sequences:
            if num > sequence[-1]:
                sequence.append(num)
                break
        else:
            sequences.append([num])
print(len(sequences))
for sequence in sequences:
    print(" ".join(map(str, sequence)))