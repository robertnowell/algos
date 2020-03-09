def majority(arr):
	if len(arr) == 0:
		return -1
	hits = 1
	misses = 0
	cand = arr[0]
	i = 1
	while i < len(arr):
		if arr[i] == cand:
			hits += 1
		else:
			misses+=1
			if misses >= hits:
				cand = arr[i]
				hits = 1
				misses = 0
		i+=1
	cands = [c for c in arr if c == cand]
	candsLen = len(cands)
	majority = len(arr) / 2
	return -1 if candsLen <= majority else cand

if __name__ == '__main__':
	print(majority([1,2,5,9,5,9,5,5,5]))