def maxSumOfContiguousSubarray(l):
	b = [0] # b[i] = sum of l[j] from j = 0 to i - 1
	for i in range(len(l)):
		b.append(b[i] + l[i])

	minIndex = 0
	result = 0, 0
	for i in range(len(b)):
		minIndex = i if b[i] < b[minIndex] else minIndex
		result = (minIndex, i) if b[i] - b[minIndex] > b[result[1]] - b[result[0]] else result
	# returning the biggest difference b[j] - b[i] for i < j. which is the biggest sum of l[k] from k = i to j - 1
	return b[result[1]] - b[result[0]]

l = [int(x) for x in input().split()]
print(maxSumOfContiguousSubarray(l))
