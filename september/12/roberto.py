class Node:
	def __init__(self, value=None, left=None, right=None, parent=None):
		self.value = value
		self.left = left
		self.right = right
		self.parent = parent

	def addLeft(self, left):
		self.left = left
		left.parent = self

	def addRight(self, right):
		self.right = right
		right.parent = self

def successor(node):
	trav = node
	if (trav.right):
		trav = trav.right
		while (trav.left):
			trav = trav.left
		return trav
	while (trav.parent and trav.parent.value < trav.value):
		trav = trav.parent
	return trav.parent

root = Node(4)
root.addLeft(Node(2))
root.addRight(Node(6))
root.left.addLeft(Node(1))
root.left.addRight(Node(3))
root.right.addLeft(Node(5))
root.right.addRight(Node(7))

print(successor(root.left.left).value)
