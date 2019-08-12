def exists(board, word):
	visited = set()
	directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

	def valid(i, j):
		return 0 <= i < len(board) and 0 <= j < len(board[i])

	def getNeighbors(i, j):
		return [(i + d[0], j + d[1]) for d in directions if valid(i + d[0], j + d[1])]

	def wordAt(i, j, word, index=0):
		if (board[i][j] != word[index]):
			return False
		if ((i, j) in visited):
			return False
		if (index == len(word) - 1):
			return True
		visited.add((i, j))
		neighbors = getNeighbors(i, j)
		for k, l in neighbors:
			if wordAt(k, l, word, index+1):
				return True
		visited.remove((i, j))
		return False

	for i in range(len(board)):
		for j in range(len(board[i])):
			if wordAt(i, j, word):
				return True

	return False

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

print(exists(board, "ABCCED"))
print(exists(board, "SEE"))
print(exists(board, "ABCB"))
