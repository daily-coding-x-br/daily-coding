def maxProfit(l):
	result = (0, 0)
	minIndex = 0
	for i in range(len(l)):
		minIndex = i if l[i] < l[minIndex] else minIndex
		result = (minIndex, i) if l[i] - minIndex > l[result[1]] - l[result[0]] else result
	return l[result[1]] - l[result[0]]

l = [int(x) for x in input().split()]
print(maxProfit(l))
