def contig(a, sum, start, end):
	if (start > end):
		return sum
	if (start == end):
		return Math.max(sum + a[start], sum)
	else:
		return Math.max(
			contig(a, sum+a[start], start+1, end-1),
			Math.max(
				contig(a, sum+a[end], start+1, end-1),
				contig(a, sum+a[start]+a[end], start+1, end-1))
