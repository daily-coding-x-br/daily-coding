def powerSet(l, i=0): # recursive
	if (i == len(l)):
		return [[]]
	rest = powerSet(l, i+1)
	result = []
	for set in rest:
		result.append(set)
		result.append(set + [l[i]])
	return result

def powerSet2(l): # iterative
	result = [[]]
	result2 = []
	for e in l:
		for set in result:
			result2.append(set)
			result2.append(set + [e])
		result = result2
		result2 = []
	return result

l = [int(x) for x in input().split()]
print(powerSet2(l))
