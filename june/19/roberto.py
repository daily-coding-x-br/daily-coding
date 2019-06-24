class Node:
	def __init__(self, value):
		self.value = value
		self.right = None
		self.left = None

def reconstruct(preorder, inorder):
	first = preorder[0]
	root = Node(first)
	if (len(preorder) == 1):
		return root
	i = 0
	while (i < len(inorder) and inorder[i] != first):
		i += 1
	root.left = reconstruct(preorder[1:i+1], inorder[:i])
	root.right = reconstruct(preorder[i+1:], inorder[i+1:])
	return root

def printTree(root, i=0):
	if root is None:
		return
	printTree(root.left, i+1)
	printTree(root.right, i+1)
	print(root.value, i)


preorder = input().split()
inorder = input().split()
root = reconstruct(preorder, inorder)
printTree(root)
