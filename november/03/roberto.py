def intersection_area(a, b):
	aMin = a.top_left
	aMax = [a.top_left[i] + a.dimensions[i] for i in range(2)]
	bMin = b.top_left
	bMax = [b.top_left[i] + b.dimensions[i] for i in range(2)]
	cMin = [max(aMin[i], bMin[i]) for i in range(2)]
	cMax = [min(aMax[i], bMax[i]) for i in range(2)]
	return max(0, (cMax[0] - cMin[0]) * (cMax[1] - cMin[1]) )
