class HitCounter:
	def __init__(self):
		self.count = 0
		self.d = {}

	def record(self, timestamp):
		self.count += 1
		self.d[timestamp] = self.count

	def total(self):
		return self.count

	def range(self, lower, upper):
		return self.d[upper] - self.d[lower] + 1

hc = HitCounter()
print(hc.total())
hc.record(1)
print(hc.total())
hc.record(2)
print(hc.total())
hc.record(3)
print(hc.total())
print(hc.range(2,3))
