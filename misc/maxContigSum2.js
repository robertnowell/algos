/*
*	sum += current elem
*	if sumsofar < 0: set sumsofar to current elem
* 	
*/
function maxContig(a) {
	maxSum = 0;
	curSum = 0;
	a.forEach((e) => {
		curSum += e;
		curSum = curSum < 0 ? e : curSum;
		maxSum = curSum > maxSum ? curSum : maxSum;
	})
	return maxSum;
};

console.log(maxContig([1,2,-4,1, 3,-2,3,-1]));