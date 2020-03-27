let cache = {};

function calcsum(a, i, j, w, l) {
	let key = [i, j, w, l];
	// console.log(key);
	if (key in cache){
		console.log("cache hit");
		return cache.key;
	}
	// console.log(i, w, j, l);
	let s = 0;
	a.slice(i,i+l+1).forEach( (r) => {
		r.slice(j, j+l+1).forEach( v => s += v );
	});
	cache[key] = s;
	return cache[key];
	// return s;
}

function calcMaxFromStartingPosition(a, i, j){
	let max = 0;
	let rows = a.length;
	let cols = a[i].length;
	for (let ii = i; ii < a.length; ii++){
		for (let jj = j; jj < a[ii].length; jj++){
			let sum = calcsum(a, i, j, ii-i, jj-j);
			max = Math.max(max, sum);
		}
	}
	return max;
}

function maxSubMatrix(a){
	let maxSum = 0
	let curSum = 0
	a.forEach((r, i) => {
		r.forEach((v, j)=> {
			let maxFromHere = calcMaxFromStartingPosition(a, i, j);
			if (maxFromHere > maxSum) {
				maxSum = maxFromHere;
				console.log(maxSum, i, j);
			}
		});
	});
	// console.log(cache);
	return maxSum;
}

arr = [
	[-5, -6, 2, 1, -1],
	[-1, -1, -1, -1, -1],
	[6, 6, 6, 6, 6],
	[-1, -1, 2, -1, 2],
	[3, 2, 1, 0, -1],
];

console.log(maxSubMatrix(arr));
