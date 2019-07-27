class Node:
	def __init__(self, value=0, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def invert(root):
	if root is None:
		return
	root.left, root.right = root.right, root.left
	invert(root.left)
	invert(root.right)

def inorderPrint(root):
	if (root is None):
		return
	inorderPrint(root.left)
	print(root.value)
	inorderPrint(root.right)

root = Node('a', Node('b', Node('d'), Node('e', Node('g'), Node('h'))), Node('c', Node('f', None, Node('i')), None))
inorderPrint(root)
print("\n")
invert(root)
inorderPrint(root)
