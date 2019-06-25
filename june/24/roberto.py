class Queue:
	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	def push(self, value):
		self.stack2.append(value)

	def pop(self):
		if (len(self.stack1) == 0):
			while (len(self.stack2) > 0):
				self.stack1.append(self.stack2.pop())
		return self.stack1.pop()

q = Queue()
n = int(input())
for i in range(n):
	if (input() == "a"):
		q.push(input())
	else:
		q.pop()
