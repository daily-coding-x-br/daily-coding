class log:
	def __init__(self, n):
		self.n = n
		self.l = [0]*n
		self.start = 0
		self.end = 0
		self.count = 0

	def record(self, id): # O(1) time
		l[end] = id
		end += 1
		end %= n
		if (count < n):
			count += 1
		else:
			start += 1
			start %= n

	def get_last(self, i): # O(1) time
		return l[(start+i)%n]
