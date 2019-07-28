class Node:
	def __init__(self, value=0, next=None):
		self.value = value
		self.next = next

def reverse(node):
	if (node.next is None):
		return
	a = node
	b = a.next
	c = b.next
	a.next = None
	while (c):
		b.next = a
		a = b
		b = c
		c = c.next
	b.next = a
	return b

def printNode(node):
	if (node is None):
		return
	print(node.value)
	printNode(node.next)

root = Node(1, Node(2, Node(3, Node(4))))
printNode(root)
root = reverse(root)
printNode(root)
