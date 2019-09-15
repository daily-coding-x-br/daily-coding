class Node:
	def __init__(self, value=None, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def minimumPathSum(node):
	if (not node):
		return 0, []
	leftPath = minimumPathSum(node.left)
	rightPath = minimumPathSum(node.right)
	path = None
	if (not node.left):
		path = rightPath
	elif (not node.right):
		path = leftPath
	else:
		path = leftPath if leftPath[0] < rightPath[0] else rightPath
	return path[0] + node.value, [node.value] + path[1]

root = Node(10, Node(5, Node(2)), Node(5, None, Node(1, Node(-1))))
print(minimumPathSum(root))
