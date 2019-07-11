def largestKProduct(l, k=3, i=0, sign=1, d={}):
	if (k == 0 or i == len(l)):
		return 1
	keep = l[i] * largestKProduct(l, k-1, i+1, sign if l[i] > 0 else -sign)
	skip = largestKProduct(l, k, i+1, sign)
	d[k, i, sign] = max(keep, skip) if sign == 1 else min(keep, skip)
	return d[k, i, sign]

l = [int(x) for x in input().split()]
print(largestKProduct(l))
