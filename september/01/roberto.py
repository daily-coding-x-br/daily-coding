def maxCoins(matrix, i=0, j=0, d={}):
	if (i >= len(matrix) or j >= len(matrix[i])):
		return 0
	if (i, j) in d:
		return d[i, j]
	d[i, j] = matrix[i][j] + max(maxCoins(matrix, i, j+1, d), maxCoins(matrix, i+1, j, d))
	return d[i, j]

n = int(input())
matrix = []
for i in range(n):
	matrix.append([int(x) for x in input().split()])
print(maxCoins(matrix))
