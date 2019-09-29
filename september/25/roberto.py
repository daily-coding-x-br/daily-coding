class Node:
	def __init__(self, value=None, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __str__(self):
		return "(" + str(self.value) + ", " + str(self.left) + ", " + str(self.right) + ")"

def prune(node):
	if not node:
		return True, node
	left = prune(node.left)
	node.left = left[1]
	right = prune(node.right)
	node.right = right[1]
	if (left[0] and right[0] and node.value == 0):
		return True, None
	return False, node

root = Node(0, Node(1), Node(0, Node(1, Node(0), Node(0)), Node(0)))
root = prune(root)[1]
print(root)
