def multisetPartition(s, i=0, k=0, memory={}):
	if (i > len(s) - 1):
		if (k == 0):
			return [], True
		else:
			return [], False
	if (i, k) in memory:
		return memory[(i, k)]
	if (k < 0):
		include = multisetPartition(s, i+1, k + s[i], memory)
		if (include[1] == True):
			memory[(i, k)] = [s[i]] + include[0], True
			return memory[(i, k)]
		skip = multisetPartition(s, i+1, k - s[i], memory)
		if (skip[1] == True):
			memory[(i, k)] = skip
			return memory[(i, k)]
	else:
		skip = multisetPartition(s, i+1, k - s[i], memory)
		if (skip[1] == True):
			memory[(i, k)] = skip
			return memory[(i, k)]
		include = multisetPartition(s, i+1, k + s[i], memory)
		if (include[1] == True):
			memory[(i, k)] = [s[i]] + include[0], True
			return memory[(i, k)]
	return [], False

s = [int(x) for x in input().split()]
print(multisetPartition(s))
