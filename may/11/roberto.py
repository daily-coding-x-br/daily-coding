def nonAdjacentLargestSum(l, i=0, d={}):
	if (i >= len(l)):
		return 0
	if (i in d):
		return d[i]
	keep = l[i] + nonAdjacentLargestSum(l, i+2)
	discard = nonAdjacentLargestSum(l, i+1)
	d[i] = max(keep, discard)
	return d[i]

l = [int(s) for s in input().split()]
print(nonAdjacentLargestSum(l))
