directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

def valid(m, k, l):
	return 0 <= k < m and 0 <= l < m

def getNeighbors(m, i, j):
	result = []
	for di, dj in directions:
		for length in range(1, m):
			k, l = i + di*length, j + dj*length
			if (not valid(m, k, l)):
				break
			result.append((k, l))
	return result

def countAttackingBishopPairs(m, l):
	board = [[False] * m for i in range(m)]
	for (i, j) in l:
		board[i][j] = True

	count = 0
	for (i, j) in l:
		neighbors = getNeighbors(m, i, j)
		for (k, l) in neighbors:
			if (board[k][l] == True):
				count += 1

	return count//2

m = int(input())
n = int(input())
l = []
for i in range(n):
	l.append([int(x) for x in input().split()[:2]])
print(countAttackingBishopPairs(m, l))
