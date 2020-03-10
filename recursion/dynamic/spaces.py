def addSpaces(arr, i, lastSpace, countSoFar):
	if i == len(arr) - 1:
		return (arr, countSoFar + countUnrecognized(arr, lastSpace+1, i+1))
	arr.insert(i+1, ' ')
	unrecognized = countUnrecognized(arr, lastSpace+1, i+1)
	arr1, withSpace = addSpaces(arr, i + 2, i+1, countSoFar+unrecognized)
	print(arr1[i+1:], withSpace)
	del arr[i+1]

	arr2, withoutSpace = addSpaces(arr, i + 1, lastSpace, countSoFar)
	print(arr2[lastSpace+1:], withoutSpace)
	return (arr1, withSpace) if withSpace < withoutSpace else (arr2, withoutSpace)

def countUnrecognized(arr, start, end):
	string = ''.join(map(str, arr[start:end]))
	if string == 'like':
		return 0
	else:
		# print (arr, start, end, string, len(string))
		return len(string)

if __name__ == '__main__':
	print(addSpaces(['l', 'i', 'k', 'e'], 0, -1, 0))
