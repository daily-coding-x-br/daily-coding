def overlap(a, b):
	aMin = a.top_left
	aMax = [a.top_left[i] + a.dimensions[i] for i in range(2)]
	bMin = b.top_left
	bMax = [b.top_left[i] + b.dimensions[i] for i in range(2)]
	if (aMin[0] > bMax[0] or bMin[0] > bMax[0]): return False
	if (aMin[1] > bMax[1] or bMin[1] > bMax[1]): return False
return True 

def any_overlap(l):
	for i in range(len(l)):
		for j in range(i, len(l)):
			if (overlap(l[i], l[j]):
				return True
	return False
