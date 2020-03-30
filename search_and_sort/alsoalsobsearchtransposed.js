let findOffset = a => {
	/*
		cases:
			-offset 0
			-end val the same as first

		during for loop
			-search left half if mid value less than first
				-mid if mid less than high else mid-1
			-else search right
	*/
	let low = 0;
	let high = a.length-1;
	let first = a[0];
	let mid;
	if (first < a[high]){
		return 0;
	}
	while (first == a[high] && high != 0){
		high--;
	}
	while (low <= high){
		mid = Math.floor((low+high)/2);
		if (first > a[mid]){
			high = mid == high ? mid-1 : mid;
		} else{
			low = mid+1;
		}
	}
	return mid;
}

let bsearchOffset = (a, n, offset) => {
	let low;
	let high;
	if (offset === 0){
		low = 0;
		high = a.length-1;
	} else if (a[a.length-1] < n){
		low = 0;
		high = offset-1;
	} else {
		low = offset;
		high = a.length-1;
	}
	console.log(a);
	while (low <= high){
		let mid = Math.floor((low + high)/2);
		val = a[mid];
		console.log(val, mid, low, high);
		if (val == n){
			return mid;
		} else if (val < n) {
			low = mid+1;
		} else {
			high = mid-1;
		}
	}
	return -1;
}

let search = (a, n) => {
	let offset = findOffset(a)
	// return offset
	return bsearchOffset(a, n, offset)
}

let arr = [1, 2, 3, 4, 5, 5, 5];
console.log(search(arr, 2));

 arr = [5, 6, 7, 1, 2, 3, 4, 5, 5, 5];
console.log(search(arr, 2));

 arr = [5, 6, 6, 7, 1, 2, 3, 4, 5, 5, 5];
console.log(search(arr, 9));

 arr = [5, 6, 7, 1, 1, 1, 1, 2, 3, 4, 5, 5, 5];
console.log(search(arr, 7));

 arr = [5, 6, 7, 8, 10, 23, 1, 2, 3, 4, 4, 4, 5, 5, 5];
console.log(search(arr, 5));
