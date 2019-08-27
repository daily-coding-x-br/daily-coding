class Node:
	def __init__(self, value=None, next=None):
		self.value = value
		self.next = next

def isPalindrome(node):
	def getLength(node):
		trav = node
		result = 0
		while (trav):
			trav = trav.next
			result += 1
		return result

	n = getLength(node)
	def helper(i=0, current=node):
		if (n%2 == 1 and i == n//2):
			return helper(i+1, current.next)
		if (i < n//2):
			answer = helper(i+1, current.next)
			if (answer[0] == False or answer[1].value != current.value):
				return False, answer[1].next
			return True, answer[1].next
		if (i >= n//2):
			return True, current

	return helper()[0]

root = Node(5, Node(3, Node(3, Node(5))))
print(isPalindrome(root))
root = Node(5, Node(3, Node(4, Node(3, Node(5)))))
print(isPalindrome(root))
