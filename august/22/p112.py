class Node:
	def __init__(self, value=None, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right
		self.parent = None
		if (left):
			self.left.parent = self
		if (right):
			self.right.parent = self

	def len(self):
		trav = self
		count = 0
		while (trav):
			trav = trav.parent
			count += 1
		return count

def getLCA(a, b):
	lenA = a.len()
	lenB = b.len()

	low, high = (a, b) if lenA > lenB else (b, a)
	for i in range(abs(lenA - lenB)):
		low = low.parent
	
	while (low != high):
		low = low.parent
		high = high.parent
	return low

a = Node(4)
b = Node(6)
node = Node(1, Node(2, Node(3, a, Node(5, b))), Node(3))
print(getLCA(a, b).value)
