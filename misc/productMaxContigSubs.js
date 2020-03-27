/*
*	product
*/
function maxContig(a) {
	best = null;
	curMax = null;
	curMin = null;
	a.forEach((e) => {
		if (best == null){
			best = curMax = curMin = e;
		} else if (e > 0) {
			curMax = Math.max(curMax*e, e);
			curMin = Math.min(curMin*e, e);
		} else {
			tmp = curMax;
			curMax = Math.max(curMin*e, e);
			curMin = Math.min(tmp*e, e);
		}
		best = Math.max(best, curMax);
		console.log(e, curMin,curMax, best);
	})
	return best;
};

let a = [6, -3, -10, 0, 2];
console.log(maxContig(a));
let b = [-1, -3, -10, 0, 60];
console.log(maxContig(b));
let c = [-2, -3, 0, -2, -40];
console.log(maxContig(c));
