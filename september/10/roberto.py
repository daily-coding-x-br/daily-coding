class Node:
	def __init__(self, value=None, next=None):
		self.value = value
		self.next = next

def getNode(travClone, trav, node):
	while (trav != node):
		trav = trav.next
		travClone = travClone.next
	return travClone

def deepClone(root):
	if (root is None):
		return None
	rootClone = Node()

	trav = root
	travClone = rootClone
	while (trav.next):
		travClone.next = Node()
		travClone = travClone.next
		trav = trav.next

	trav = root
	travClone = rootClone
	while (trav):
		travClone.value = getNode(travClone, trav, trav.value)
		travClone = travClone.next
		trav = trav.next
	return rootClone

def deepClone2(root):
	if (root is None):
		return None
	rootClone = Node()
	d = {}

	trav = root
	travClone = rootClone
	d[root] = rootClone
	while (trav.next):
		travClone.next = Node()
		travClone = travClone.next
		trav = trav.next
		d[trav] = travClone

	trav = root
	travClone = rootClone
	while (trav):
		travClone.value = d[trav.value] if trav.value else None
		travClone = travClone.next
		trav = trav.next
	return rootClone

def printNode(node):
	if (not node):
		return
	print("node = " + str(node))
	print("node.value = " + str(node.value))
	print("node.next = " + str(node.next))
	print(" ")
	printNode(node.next)

n3 = Node()
n2 = Node(None, n3)
n1 = Node(n3, n2)

l = deepClone2(n1)
printNode(n1)
print("\n")
printNode(l)
