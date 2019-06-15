class Stack:
	def __init__(self):
		self.stack = [] # list of integers
		self.maxStack = [] # list of pairs (integer, count)

	def push(item):
		if (item > stack.peek()):
			if (item == maxStack.peek()[0]):
				min = maxStack.pop()
				min[1] += 1
				maxStack.push(min)
			else:
				maxStack.push(item, 1)
		stack.push(item)

	def pop():
		result = stack.pop()
		if (result == maxStack.peek()[0]):
			min = maxStack.pop()
			min[1] -= 1
			if (min[1] != 0):
				maxStack.push(item, 1)
		return result

	def max():
		return maxStack.peek()
