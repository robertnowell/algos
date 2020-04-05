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

3x + 2y + z = 4(x+y+z) - (x + 2y + 3z)

calculate regular sum and weighted sum by recursing through as in depthsum
multiply unweighted sum by max level + 1
subtract weighted sum
*/
sums = {
    uw: 0,
    w: 0,
};

let recurse = (a, i, d)=>{
    if (i >= a.length) {
        return d;
    }
    console.log(a[i])
    let md = d;
    if (Array.isArray(a[i])){
        md = recurse(a[i], 0, d+1);
    } else {
        sums.uw += a[i];
        sums.w += a[i]*d;
    }
    md = Math.max(md, recurse(a, i+1,d));
    return md;
}

let revDepthSum = (arr) => {
    maxDepth = 0;
    let md = recurse(arr, 0, 1);
    console.log(md);
    console.log(sums);
    console.log(sums.uw*(md+1) - sums.w);
    
}

revDepthSum([[1,2],3,[4,[6], 5]]);