class Sudoku:
	def __init__(self, board = None):
		# board is a 9 x 9 matrix. Cells are filled with either a digit from 1 to 9 or 0, which represents an empty cell.
		if (board):
			self.board = board
		else:
			self.board = [[0] * 9 for i in range(9)]

	def empty(self, x, y):
		return self.board[y][x] == 0

	def conflict(self, x, y, n):
		for i in range(9):
			if (board[i][x] == n and i != y):
				return True

		for j in range(9):
			if (board[y][j] == n and j != x):
				return True

		for i, j in self.getSquare(x, y):
			if (board[i][j] == n and (i, j) != (y, x)):
				return True
		return False

	def getSquare(self, x, y):
		return [((y//3)*3 + i, (x//3)*3 + j) for i in range(3) for j in range(3)]

	def solve(self, i=0):
		if (i == 9*9):
			print("Solved")
			return True
		x = i%9
		y = i//9
		if not self.empty(x, y):
			return self.solve(i + 1)

		for n in range(1, 10):
			if (self.conflict(x, y, n)):
				continue
			board[y][x] = n
			if self.solve(i + 1):
				return True
			board[y][x] = 0
		return False

	def printBoard(self):
		for i in range(9):
			for j in range(9):
				print(str(board[i][j]) + " ", end="")
			print("")


board = []
for i in range(9):
	board.append([int(x) for x in input().split()])
sudoku = Sudoku(board)
sudoku.printBoard()
sudoku.solve()
sudoku.printBoard()
