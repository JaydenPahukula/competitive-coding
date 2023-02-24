import heapq
import sys

sys.stdin=open("mootube.in","r")
sys.stdout=open("mootube.out","w")

N, Q = map(int, input().split())

connections = [[] for _ in range(N)]
for _ in range(N-1):
    p, q, relevance = map(int, input().split())
    connections[q-1].append((p-1, relevance))
    connections[p-1].append((q-1, relevance))

for _ in range(Q):
    minRelevance, startVid = map(int, input().split())
    numDiscovered = 0
    q = [(startVid-1, 10e9, -1)]
    while q:
        currVid, currRelevance, lastVid = q.pop()

        for vid, relevance in connections[currVid]:
            if vid == lastVid: continue
            if min(relevance, currRelevance) >= minRelevance:
                numDiscovered += 1
                q.append((vid, min(relevance, currRelevance), currVid))
    