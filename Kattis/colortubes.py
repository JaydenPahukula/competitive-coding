from collections import deque

n = int(input())
tubes = [[int(x) for x in input().split() if x != "0"] for _ in range(n+1)]
locations = [[0 for _ in range(n+1)] for _ in range(n+1)]
for tube in range(n+1):
	for color in tubes[tube]:
		locations[color][tube] += 1
moves = deque()

def move(a, b):
	moves.append((a+1, b+1))
	color = tubes[a].pop()
	tubes[b].append(color)
	locations[color][a] -= 1
	locations[color][b] += 1
	print(tubes)

# make empty tube
emptyTube = -1
t1, t2 = -1, -1
for tube in range(n+1):
	if len(tubes[tube]) == 0:
		emptyTube = tube
		break
	elif len(tubes[tube]) == 1:
		t1 = tube
	elif len(tubes[tube]) == 2:
		t2 = tube
else:
	move(t1, t2)
	emptyTube = t1

tubesRemaining = {x for x in range(n+1)}
while len(tubesRemaining) > 1:
	tube1 = -1
	for tube in range(n+1):
		if tube != emptyTube and tube in tubesRemaining:
			tube1 = tube
			break
	color = tubes[tube1][2]
	if locations[color][tube1] == 3:
		# case 0 (done)
		tubesRemaining.remove(tube1)
	elif locations[color][tube1] == 2:
		# cases 1-6
		tube2 = -1
		for tube in range(n+1):
			if locations[color][tube] == 1:
				tube2 = tube
				break
		if tubes[tube1][0] == color:
			if tubes[tube2][0] == color: # case 1
				move(tube2, emptyTube)
				move(tube2, emptyTube)
				move(tube1, tube2)
				move(tube1, emptyTube)
				move(tube1, tube2)
				tubesRemaining.remove(emptyTube)
				emptyTube = tube1
			elif tubes[tube2][1] == color: # case 2
				move(tube1, emptyTube)
				move(tube2, tube1)
				move(tube2, emptyTube)
				move(tube1, tube2)
				move(tube1, tube2)
				move(tube1, emptyTube)
				tubesRemaining.remove(emptyTube)
				emptyTube = tube1
			else: # case 3
				move(tube1, emptyTube)
				move(tube2, emptyTube)
				move(tube1, tube2)
				move(tube1, emptyTube)
				tubesRemaining.remove(emptyTube)
				emptyTube = tube1
		else:
			if tubes[tube2][0] == color: # case 4
				move(tube1, emptyTube)
				move(tube1, emptyTube)
				move(tube2, tube1)
				move(tube2, tube1)
				move(tube2, emptyTube)
				tubesRemaining.remove(emptyTube)
				emptyTube = tube2
			elif tubes[tube2][1] == color: # case 5
				move(tube1, emptyTube)
				move(tube1, emptyTube)
				move(tube2, tube1)
				move(tube2, emptyTube)
				move(tube2, tube1)
				tubesRemaining.remove(emptyTube)
				emptyTube = tube2
			else: # case 6
				move(tube1, emptyTube)
				move(tube1, emptyTube)
				move(tube2, emptyTube)
				move(tube1, tube2)
				tubesRemaining.remove(emptyTube)
				emptyTube = tube1
	else:
		# cases 7-18
		tube2, tube3 = -1, -1
		for tube in range(n+1):
			if locations[color][tube] == 2:
				tube2 = tube
				break
			elif locations[color][tube] == 1 and tube != tube1:
				if tube2 == -1:
					tube2 = tube
				else:
					tube3 = tube
					break
		if tube3 == -1:
			# cases 7-9
			if tubes[tube2][2] == color and tubes[tube2][1] == color: # case 7
				move(tube1, emptyTube)
				move(tube2, emptyTube)
				move(tube2, emptyTube)
				move(tube2, tube1)
				tubesRemaining.remove(emptyTube)
				emptyTube = tube2
			elif tubes[tube2][2] == color and tubes[tube2][0] == color: # case 8
				move(tube1, emptyTube)
				move(tube2, emptyTube)
				move(tube2, tube1)
				move(tube2, emptyTube)
				tubesRemaining.remove(emptyTube)
				emptyTube = tube2
			else: # case 9
				move(tube1, emptyTube)
				move(tube2, tube1)
				move(emptyTube, tube2)
				tubesRemaining.remove(2)
		else:
			# cases 10-18
			if tubes[tube2][2] == color:
				if tubes[tube3][2] == color: # case 10
					move(tube1, emptyTube)
					move(tube2, emptyTube)
					move(tube3, emptyTube)
					move(tube1, tube2)
					move(tube1, tube3)
					tubesRemaining.remove(emptyTube)
					emptyTube = tube1
				elif tubes[tube3][1] == color: # case 11
					move(tube1, emptyTube)
					move(tube2, emptyTube)
					move(tube3, tube1)
					move(tube3, emptyTube)
					move(tube3, tube2)
					tubesRemaining.remove(emptyTube)
					emptyTube = tube3
				else: # case 12
					move(tube1, emptyTube)
					move(tube2, emptyTube)
					move(tube3, tube1)
					move(tube3, tube2)
					move(tube3, emptyTube)
					tubesRemaining.remove(emptyTube)
					emptyTube = tube3
			elif tubes[tube2][1] == color:
				if tubes[tube3][2] == color: # case 13
					move(tube1, emptyTube)
					move(tube3, emptyTube)
					move(tube2, tube1)
					move(tube2, emptyTube)
					move(tube2, tube3)
					tubesRemaining.remove(emptyTube)
					emptyTube = tube2
				elif tubes[tube3][1] == color: # case 14
					move(tube1, emptyTube)
					move(tube2, tube1)
					move(tube2, emptyTube)
					move(tube3, tube2)
					move(tube3, emptyTube)
					move(tube3, tube2)
					tubesRemaining.remove(emptyTube)
					emptyTube = tube3
				else: # case 15
					move(tube3, emptyTube)
					move(tube3, emptyTube)
					move(tube1, tube3)
					move(tube2, tube1)
					move(tube2, tube3)
					move(tube2, emptyTube)
					tubesRemaining.remove(tube3)
					emptyTube = tube2
			else:
				if tubes[tube3][2] == color: # case 16
					move(tube1, emptyTube)
					move(tube3, emptyTube)
					move(tube2, tube1)
					move(tube2, tube3)
					move(tube2, emptyTube)
					tubesRemaining.remove(emptyTube)
					emptyTube = tube2
				elif tubes[tube3][1] == color: # case 17
					move(tube2, emptyTube)
					move(tube2, emptyTube)
					move(tube1, tube2)
					move(tube3, emptyTube)
					move(tube3, tube2)
					move(tube3, tube1)
					tubesRemaining.remove(tube2)
					emptyTube = tube3
				else: # case 18
					move(tube3, emptyTube)
					move(tube3, emptyTube)
					move(tube1, tube3)
					move(tube2, emptyTube)
					move(tube2, tube1)
					move(tube2, tube3)
					tubesRemaining.remove(tube3)
					emptyTube = tube2
print(len(moves))
for a, b in moves:
	print(a, b)