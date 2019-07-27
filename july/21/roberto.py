class Node:
	def __init__(self, value=0, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def deepestNode(root):
	def deepestNodeAndHeight(root, h=0):
		if (root is None):
			return None, 0
		left = deepestNodeAndHeight(root.left, h+1)
		right = deepestNodeAndHeight(root.right, h+1)
		if (root.left is None and root.right is None):
			return root, h
		if (left[1] >= right[1]):
			return left
		else:
			return right
	return deepestNodeAndHeight(root)[0]

root = Node("a", Node("b", Node("d")), Node("c"))
print(deepestNode(root).value)
