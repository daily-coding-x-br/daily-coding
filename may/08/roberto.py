class Node:
	def __init__(self, val, both):
		self.val = val
		self.both = both

class XOR_list:
	def __init__(self):
		self.head = None

	def add(element):
		if (head is None):
			head = Node(element, 0^0)
		else:
			trav = head
			next_addr = trav.both^0
			while (next_addr != 0):
				last = get_pointer(trav)
				trav = dereference_pointer(next_addr)
				next_addr = trav.both^last
			last = get_pointer(trav)
			tail = Node(element, last^0)
			trav.both ^= 0
			trav.both ^= get_pointer(tail)

	def get(index):
		if head is None: return -1
		trav = head
		next_addr = trav.both^0
		for i in range(index):
			last = get_pointer(trav)
			trav = dereference_pointer(next_addr)
			next_addr = trav.both^last
		return trav.val
