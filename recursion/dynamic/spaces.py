memo = {}

def addSpaces(arr, i, lastSpace, countSoFar):
	# also terminate once arr[lastSpace+1:i] cannot lead to a word
	key = tuple(arr[lastSpace+1:])
	if i == len(arr) - 1 and key not in memo:
		memo[key] = (arr, countSoFar + countUnrecognized(arr, lastSpace+1, i+1))
	if key in memo:
		print("memo saved us time: ", key, memo[key])
		return memo[key]

	arr.insert(i+1, ' ')
	unrecognized = countUnrecognized(arr, lastSpace+1, i+1)
	arr1, withSpace = addSpaces(arr, i + 2, i+1, countSoFar+unrecognized)
	print(arr1[i+1:], withSpace)
	del arr[i+1]

	arr2, withoutSpace = addSpaces(arr, i + 1, lastSpace, countSoFar)
	print(arr2[lastSpace+1:], withoutSpace)
	memo[key] = (arr1, withSpace) if withSpace < withoutSpace else (arr2, withoutSpace)
	return memo[key]

def countUnrecognized(arr, start, end):
	string = ''.join(map(str, arr[start:end]))
	if string == 'like':
		return 0
	else:
		# print (arr, start, end, string, len(string))
		return len(string)

if __name__ == '__main__':
	print(addSpaces(['l', 'i', 'k', 'e'], 0, -1, 0))
	for k in memo:
		print(k, memo[k])
