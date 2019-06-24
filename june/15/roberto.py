# Binary search tree. Each time we add one element to the left, increase the counter by the number of elements to the right + 1 (the parent).
# O(n) space, O(nlog(n)) average time, O(n^2) worst case time

class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.childrenCount = 1

	def rightChildrenCount(self):
		return self.right.childrenCount if self.right else 0

def insert(node, value):
	node.childrenCount += 1
	if node.value < value:
		if (node.right):
			return insert(node.right, value)
		else:
			node.right = Node(value)
			return 0
	else: # value < node.value
		if (node.left):
			return 1 + node.rightChildrenCount() + insert(node.left, value)
		else:
			node.left = Node(value)
			return 1 + node.rightChildrenCount()

def countInversions(l):
	count = 0
	root = Node(l[0])
	for i in range(1, len(l)):
		count += insert(root, l[i])
	return count

l = [int(x) for x in input().split()]
print(countInversions(l))
