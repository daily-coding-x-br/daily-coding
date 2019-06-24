class Node:
	def __init__(self, value, right=None, left=None):
		self.value = value
		self.right = right
		self.left = left

def evaluate(root):
	if root.left is None: # is a leaf
		return root.value
	if (root.value == "+"):
		return evaluate(root.left) + evaluate(root.right)
	elif (root.value == "-"):
		return evaluate(root.left) - evaluate(root.right)
	elif (root.value == "*"):
		return evaluate(root.left) * evaluate(root.right)
	elif (root.value == "/"):
		return evaluate(root.left) // evaluate(root.right)

root = Node("*", Node("+", Node(3), Node(2)), Node("+", Node(4), Node(5)))
print(evaluate(root))
