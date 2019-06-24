class LRU:
	def __init__(self, n):
		self.arr = [None] * n
		self.n = n
		self.d = {}
		self.index = 0

	def set(key, value):
		if (arr[index] and arr[index] in d):
			del d[arr[index]]
		d[key] = value
		index += 1
		index %= n;

	def get(key):
		return d[key] in key in d else None
