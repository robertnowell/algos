let findOffset = a => {
	// special case no transposition
	if (a[0] < a[a.length-1]){
		return 0;
	}
	start = a[0];
	low = 0;
	high = a.length-1;
	while (start === a[high] && high > 0) { 
		high--;
	}
	console.log(a);
	while (low <= high){
		mid = Math.floor((low+high)/2)
		console.log(low, high, mid, a[mid], start)
		if (a[mid] < start)  {
			// look left
			high = high == mid ? mid-1 : mid;
		} else {
			low = mid+1;
		}
	}
	return mid;
}

let bsearchOffset = (a, n, offset) =>{
	let low;
	let high;
	if (offset == 0) {
		low = 0;
		high = a.length-1;
	} else {
		if (n > a[0]){
			low = 0;
			high = offset-1;
		} else {
			low = offset;
			high = a.length-1;
		}
	}
	while (low <= high){
		let mid = Math.floor((low + high)/2);
		if (a[mid] == n){
			return mid;
		} else if (a[mid] > n){
			// search left
			high = mid-1;
		} else {
			// search right
			low = mid+1;
		}
	}
	return -1;
}

let search = (a, n) => {
	let offset = findOffset(a)
	return bsearchOffset(a, n, offset)
}

let arr = [5, 6, 7, 1, 2, 3, 4, 5, 5, 5];
console.log(search(arr, 2));

 arr = [5, 6, 6, 7, 1, 2, 3, 4, 5, 5, 5];
console.log(search(arr, 9));

 arr = [5, 6, 7, 1, 1, 1, 1, 2, 3, 4, 5, 5, 5];
console.log(search(arr, 7));

 arr = [5, 6, 7, 8, 10, 23, 1, 2, 3, 4, 4, 4, 5, 5, 5];
console.log(search(arr, 5));
