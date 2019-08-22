from collections import deque

class Node:
	def __init__(self, value=None, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def printLevelWise(root):
	queue = deque()
	queue.append(root)
	while (queue):
		element = queue.popleft()
		print(element.value)
		if (element.left):
			queue.append(element.left)
		if (element.right):
			queue.append(element.right)

root = Node(1, Node(2), Node(3, Node(4), Node(5)))
printLevelWise(root)
