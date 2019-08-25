class Node:
	def __init__(self, value=None, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def matches(s, t):
	if ((s is None) != (t is None)):
		return False
	if (s is None and t is None):
		return True
	if (s.value != t.value):
		return False
	return matches(s.left, t.left) and matches(s.right, t.right)

def hasSubtreeThatMatches(s, t):
	if (s is None):
		return False
	return matches(s, t) or hasSubtreeThatMatches(s.left, t) or hasSubtreeThatMatches(s.right, t)

s = Node(1, Node(3, Node(2, Node(1), Node(3)), Node(5)), Node(3))
t = Node(2, Node(1), Node(3))
print(hasSubtreeThatMatches(s, t))
