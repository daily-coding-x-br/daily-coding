from queue import PriorityQueue

def merge(m):
	# m is an array of k linked lists
	k = len(m)
	minHeap = PriorityQueue()
	for i in range(k):
		linkedList = m[i]
		minHeap.put((linkedList.pop(0), i))
	result = []
	while (not minHeap.empty()):
		smallest, i = minHeap.get()
		result.append(smallest)
		linkedList = m[i]
		if (linkedList):
			minHeap.put((linkedList.pop(0), i))
	return result

k = int(input())
m = []
for i in range(k):
	m.append([int(x) for x in input().split()])
print(merge(m))
