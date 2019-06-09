def runningMedian(l):
	left = maxHeap()
	right = minHeap()
	right.add(l[0])
	median = l[0]
	print(median)
	even = True
	for i in range(1, len(l)):
		if (l[i] >= median):
			right.add(l[i])
		else:
			left.add(l[i])
		rebalance(left, right)
		if (even):
			median = left.peek() if len(left) > len(right) else right.peek()
		else:
			median = (left.peek() + right.peek())/2
		even = not even
		print(median)

def rebalance(left, right):
	if (len(left) > len(right) + 1):
		right.add(left.pop())
	else if (len(right) > len(left) + 1):
		left.add(right.pop())
