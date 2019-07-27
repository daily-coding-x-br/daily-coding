def countIslands(m):
	count = 0
	visited = [[False] * len(m[0]) for i in range(len(m))]
	neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
	def valid(i, j):
		return 0 <= i < len(m) and 0 <= j < len(m[0])

	def getNeighbors(i, j):
		return [(i + n[0], j + n[1]) for n in neighbors if valid(i + n[0], j + n[1])]

	def recurse(i, j):
		if (m[i][j] == 0 or visited[i][j]):
			return 0
		visited[i][j] = True
		for (k, l) in getNeighbors(i, j):
			recurse(k, l)
		return 1

	for i in range(len(m)):
		for j in range(len(m[0])):
			count += recurse(i, j)
	return count

m = [[1, 0, 0, 0, 0],
	[0, 0, 1, 1, 0],
	[0, 1, 1, 0, 0],
	[0, 0, 0, 0, 0],
	[1, 1, 0, 0, 1],
	[1, 1, 0, 0, 1]]

print(countIslands(m))
