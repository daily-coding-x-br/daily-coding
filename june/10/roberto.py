def conway(l, n):
	board = set()
	minX, maxX, minY, maxY = float('inf'), float('-inf'), float('inf'), float('-inf')
	directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

	for x, y in l:
		board.add((x, y))
		minX = min(x, minX)
		maxX = max(x, maxX)
		minY = min(y, minY)
		maxY = max(y, maxY)

	print(board)

	def isAlive(x, y):
		return (x, y) in board

	def printBoard():
		for y in range(minY, maxY + 1):
			for x in range(minX, maxX + 1):
				print('*' if isAlive(x, y) else '.', end = '')
			print('\n', end = '')
		print('\n', end = '')

	def getNeighbors(x, y):
		return [(x + d[0], y + d[1]) for d in directions]

	def countLiveNeighbors(x, y):
		neighbors = getNeighbors(x, y)
		count = 0
		for x, y in neighbors:
			if isAlive(x, y):
				count += 1
		return count

	def getCellsToKill():
		cellsToKill = set()
		for x, y in board:
			count = countLiveNeighbors(x, y)
			if (count < 2 or 3 < count):
				cellsToKill.add((x,y))
		return cellsToKill

	def getCellsToBeBorn():
		cellsToBeBorn = set()
		neighborCount = {}
		for x, y in board:
			for x2, y2 in getNeighbors(x, y):
				if isAlive(x2, y2): continue
				neighborCount[(x2, y2)] = 1 + (neighborCount[(x2, y2)] if (x2, y2) in neighborCount else 0)
		for x, y in neighborCount:
			if neighborCount[(x, y)] == 3:
				cellsToBeBorn.add((x, y))
		return cellsToBeBorn

	printBoard()
	for i in range(n):
		cellsToKill = getCellsToKill()

		cellsToBeBorn = getCellsToBeBorn()

		for x, y in cellsToKill:
			board.remove((x, y))

		for x, y in cellsToBeBorn:
			board.add((x, y))
		printBoard()

len = int(input())
l = []
for i in range(len):
	x, y = [int(x) for x in input().split()]
	l.append((x,y))
n = int(input())
conway(l, n)
