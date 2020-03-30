let findOffset = (a, start, end) => {
	let first = a[start]
	let mid;
	while (start <= end){
		mid = Math.floor((start + end)/2)
		console.log(a, start, mid, a[mid], end)
		if (a[mid] < first){
			end = mid-1
		} else if( start!= mid){
			start = mid
		} else if (arr[start+1] >= first) {
			start++;
		} else{
			break
		}
	}
	console.log(start, mid, end);
	// let max = mid+1
	// if (max > a.length-1){
	// 	return 0
	// }
	// return max-1
}

// if (midValue < split)
// last = mid ­ 1; // look to the left
// else if (first != mid)
// first = mid; // look to the right
// else if (list[first + 1] >= split)
// ++first;
// else
// break;

let bsearchTransposed = (a, n) => {
	let offset = findOffset(a, 0, a.length-1);
	return bSearchOffset(a, n, offset);
}

let arr = [6, 7, 1, 2, 3, 4, 5];

console.log(findOffset(arr, 0, arr.length-1))
console.log(findOffset([1, 2, 3, 4, 5, 6, 7], 0, arr.length-1))
console.log(findOffset([2, 3, 4, 5, 6, 7, 1], 0, arr.length-1))
