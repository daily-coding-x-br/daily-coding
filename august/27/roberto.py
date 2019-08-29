class Node:
	def __init__(self, value=None, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def levelWithBiggestSum(root):
	minSum, minSumIndex = float("inf"), 0
	currentSum, currentIndex = 0, 0
	stack = [root]
	currentStack = []
	while (stack):
		node = stack.pop()
		currentSum += node.value
		if node.left:
			currentStack.append(node.left)
		if node.right:
			currentStack.append(node.right)
		if (len(stack) == 0):
			stack = currentStack
			currentStack = []
			minSum, minSumIndex = (currentSum, currentIndex) if currentSum < minSum else (minSum, minSumIndex)
			currentIndex += 1
			currentSum = 0
	return minSumIndex

root = Node(1, Node(-2, Node(3)), Node(-3))
print(levelWithBiggestSum(root))
