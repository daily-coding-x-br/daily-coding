class Node:
	def __init__(self, value=None, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def twoSum(node, k, d={}):
	if (node is None):
		return None
	if k - node.value in d:
		return node, d[k - node.value]
	d[node.value] = node
	left = twoSum(node.left, k, d)
	if left:
		return left
	right = twoSum(node.right, k, d)
	if right:
		return right
	return None

root = Node(10, Node(5), Node(15, Node(11), Node(15)))
k = 20
result = twoSum(root, k)
print((result[0].value, result[1].value) if result else "None")
