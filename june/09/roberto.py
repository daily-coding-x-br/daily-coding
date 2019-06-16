def nQueens(n):
	board = [[False] * n for i in range(n)]
	count = [0]
	def getCount(i=0):
		if (i == n):
			count[0] += 1
			return
		for j in range(n):
			if not Threathened(i, j):
				board[i][j] = True
				getCount(i+1)
				board[i][j] = False
		return

	def Threathened(i, j):
		directions = [(1,0), (1,1), (0,1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
		for direction in directions:
			for length in range(1, n):
				I, J = i + direction[0] * length, j + direction[1] * length
				if (not valid(I, J)):
					break
				if (board[I][J]):
					return True
		return False

	def valid(i, j):
		return (0 <= i < n) and (0 <= j < n)

	getCount()
	return count[0]

n = int(input())
print(nQueens(n))
