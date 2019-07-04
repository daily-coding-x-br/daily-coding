# O(n*m) time, O(n*m) space
def ways(n, m, d={}):
	if (n == 1 or m == 1):
		return 1
	if ((n, m) in d):
		return d[n, m]
	d[n, m] = ways(n - 1, m, d) + ways(n, m - 1, d)
	return d[n, m]

n = int(input())
m = int(input())
print(ways(n, m))
