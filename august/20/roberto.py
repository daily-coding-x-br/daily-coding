class Node:
	def __init__(self, value=None, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def getPaths(node):
	if node is None:
		return []
	if (node.left is None and node.right is None):
		return [[node.value]]
	result = []
	for path in getPaths(node.left):
		result.append([node.value] + path)
	for path in getPaths(node.right):
		result.append([node.value] + path)
	return result

root = Node(1, Node(2), Node(3, Node(4), Node(5)))
print(getPaths(root))
