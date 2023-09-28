pa, ka, pb, kb, n = map(int, input().split())
print(" ".join(map(str, min([min([(na*pa+nb*pb, nb, na) for nb in range(100) if na*ka+nb*kb >= n]) for na in range(100)])[::-1])))