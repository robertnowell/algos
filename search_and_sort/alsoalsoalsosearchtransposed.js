/**

Question Description: Given a sorted array that has been transposed 
(that is, a portion has been removed from one end and attached to the other), 
write a function to determine if a given number is present in the array. 
Examples: [6 7 1 2 3 4 5] => find 1 or 4; [4 5 6 9 1 2 3] => find 1 or 8 
*/
let findOffset = a => {
	if (a.length == 0) {
		return 0;
	}
	if (a[0] < a[a.length-1]) {
		return 0;
	}
	let high = a.length-1;
	let low = 0;
	let start = a[0];
	while (a[high] == a[start]) {
		high--;
	}
	let mid;
	while (low <= high){
		mid = Math.floor((low + high)/2)
		if (a[mid] < start) {
			// look left
			high = high == mid ? mid-1 : mid;
		} else {
			// look right
			low = mid+1
		}
	}
	return mid;
}

let searchtransposed = (a, n) => {
	let offset = findOffset(a)
	return offset;
	return bsearchoffset(a, n, offset)
}

console.log(searchtransposed([6, 7, 1, 2, 3, 4, 5]))

let arr = [5, 6, 7, 1, 2, 3, 4, 5, 5, 5];
console.log(searchtransposed(arr, 2));

 arr = [5, 6, 6, 7, 1, 2, 3, 4, 5, 5, 5];
console.log(searchtransposed(arr, 9));

 arr = [5, 6, 7, 1, 1, 1, 1, 2, 3, 4, 5, 5, 5];
console.log(searchtransposed(arr, 7));

 arr = [5, 6, 7, 8, 10, 23, 1, 2, 3, 4, 4, 4, 5, 5, 5];
console.log(searchtransposed(arr, 5));
