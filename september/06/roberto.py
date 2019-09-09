class Node:
	def __init__(self, value=None, next=None):
		self.value = value
		self.next = next

def add(a, b):
	root = Node()
	carry = 0
	trav = root
	while (a or b or carry != 0):
		left = a.value if a else 0
		right = b.value if b else 0
		trav.next = Node((left + right + carry)%10)
		carry = (left + right + carry)//10
		trav = trav.next
		if a:
			a = a.next
		if b:
			b = b.next

	return root.next

def readLinkedList():
	l = [int(x) for x in input().split()]
	root = Node(l[0])
	trav = root
	for i in range(1, len(l)):
		trav.next = Node(l[i])
		trav = trav.next
	return root

def printLinkedList(root):
	trav = root
	while (trav):
		print(trav.value, end=" ")
		trav = trav.next

a = readLinkedList()
b = readLinkedList()
printLinkedList(add(a, b))
