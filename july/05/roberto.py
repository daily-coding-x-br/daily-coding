def countKnightTours(n):
	neighbors = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

	def valid(i, j, n):
		return (0 <= i < n and 0 <= j < n)

	def getValidNeighbors(i, j):
		return [(i+di, j+dj) for (di, dj) in neighbors if valid(i+di, j+dj, n)]

	def helper(n, i = 0, j = 0, visited = [[False] * n for i in range(n)], visitedCount = 0):
		if (visited[i][j]):
			return 0
		if (visitedCount == n*n - 1):
			return 1
		result = 0
		visited[i][j] = True
		for (k, l) in getValidNeighbors(i, j):
			result += helper(n, k, l, visited, visitedCount+1)
		visited[i][j] = False
		return result

	return helper(n)

n = int(input())
print(countKnightTours(n))
