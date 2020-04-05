/**
* Given a nested list of integers, returns the sum of all integers in the list weighted by their reversed level #.
* For example, given the list {{1,1},2,{1,{1}}} the deepest level is 2. Thus the function should return 8 (four 1's
* Given the list {1,{4,{6,2}}} the function should return 19 (1 with weight 3, 4 with weight 2, 6 with weight 1, 2
*
* It is the "reverse depth" of the item in the list: eg for the above item { 1, {4, { 6, 2 } } }
*
* 1 (reverse­depth 3) . = 1 * 3 = 3
* \
* { 4 } (reverse­depth 2) = 4 * 2 = 8
* \
* { 6, 2 } (reverse­depth 1) = 6 * 1 + 2 * 1 = 8
*
* = 3 + 8 + 8 = 19

strategies
    -pass through first time and check greatest depth'
        -then recurse and subtract from depth rather than add

    -add each successive level to a stack
        -levels aren't guaranteed to be found in order, so reversing the levels is not trivial
        -some other auxilliary datastructure e.g. map could work

    -dfs
            explore next
            visit this element
            return max
        basically
            if i > len:
                return max
            sum, maxlevelsbelow = dfs(arr, i+1, maxsofar, sum)
            sum += arr[i] * (maxlevelsbelow+1)
            return sum, maxsofar+1
*/


// let helper = (a, i, maxSoFar) => {
//     debugger;
//     if (i >= a.length){
//         let res =  {sum: 0, maxBelow: maxSoFar};
//         return res;
//     }
//     // need to branch in order to determine max level below
//     // branching condition:
//         // if current is a list, maxbelow is the max of i+1 and helper on a[i]
    
//     let sum = 0;
//     let maxBelow = maxSoFar;
//     if (Array.isArray(a[i])) {
//         let res = helper(a[i], 0, maxSoFar);
//         sum = res.sum;
//         maxBelow = res.maxBelow;
//     }
//     let result = helper(a, i+1, maxBelow);
//     let {sum: alsosum, maxBelow: alsomaxBelow} = result;
//     sum += alsosum;
//     maxBelow = Math.max(maxSoFar, alsomaxBelow);

//     if (!Array.isArray(a[i])) {
//         sum += a[i] * (maxBelow+1);
//     }
//     let res = { sum, maxBelow: maxSoFar+1};
//     return res;
// }

// let revdepthsum = (a) => {
//     let {sum, maxBelow: depth} = helper(a, 0, 0);
//     console.log(sum, depth);
// }

let sum = 0;

let revdepthsum = (a, i, d) => {
    debugger;
    if (i >= a.length) {
        return;
    }
    revdepthsum(a, i+1, d);
    if (Array.isArray(a[i])){
        revdepthsum(a[i], 0, d-1);
    } else {
        sum += a[i]*d;
    }
}

let calcDepth = (a, i, d) => {
    if (i >= a.length){
        return d;
    }

    if (Array.isArray(a[i])){
        return Math.max(calcDepth(a, i+1, d), calcDepth(a[i], 0, d+1));
    }
    return calcDepth(a, i+1, d);
}

maxDepth = calcDepth([[1,2],3,[4,[6], 5]], 0, 1);
revdepthsum([[1,2],3,[4,[6], 5]], 0, maxDepth);
console.log(sum);
