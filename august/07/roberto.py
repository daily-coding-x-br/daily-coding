class binaryTree:
	def __init__(self, time=None, left=None, right=None):
		self.time = time
		self.left = left
		self.right = right

	def add(self, time):
		if (time < self.time):
			if (self.left):
				self.left.add(time)
			else:
				self.left = binaryTree(time)
		elif (time > self.time):
			if (self.right):
				self.right.add(time)
			else:
				self.right = binaryTree(time)

	def get(self, time):
		treeTime = None
		trav = self
		while True:
			if (trav.time == time):
				return time
			elif (time < trav.time):
				if (trav.left):
					trav = trav.left
				else:
					return treeTime
			elif (time > trav.time):
				treeTime = trav.time
				if (trav.right):
					trav = trav.right
				else:
					return treeTime

class timeMap:
	def __init__(self):
		self.d = {}

	def set(self, key, value, time):
		if key not in self.d:
			self.d[key] = binaryTree(time), {}
		tree, timeHash = self.d[key]
		tree.add(time)
		timeHash[time] = value

	def get(self, key, time):
		if key not in self.d:
			return None #"key not in d"
		tree, timeHash = self.d[key]
		treeTime = tree.get(time)
		return timeHash[treeTime] if treeTime in timeHash else None #"time not in hash"

timeMap = timeMap()
while True:
	action = input()
	if (action == "set"):
		key, value, time = [int(x) for x in input().split()]
		timeMap.set(key, value, time)
	elif (action == "get"):
		key, time = [int(x) for x in input().split()]
		print(timeMap.get(key, time))
