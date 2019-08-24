def contiguousElementsSum(l, k):
	map = {}
	runningSum = 0
	for i, e in enumerate(l):
		map[runningSum] = i
		runningSum += e
		if (runningSum - k in map):
			start = map[runningSum - k]
			return l[start:i+1]
	return []

k = int(input())
l = [int(x) for x in input().split()]

print(contiguousElementsSum(l, k))
