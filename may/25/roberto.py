from collections import deque

def solution(board, start, end):
	m = len(board)
	n = len(board[0])
	q = deque()
	count = 0
	q.append((start, count))
	visited = [[False]*n for i in range(m)]
	while (q):
		current = q.popleft()
		((i, j), count) = current
		if (i == end[0] and j == end[1]):
			return count
		visited[i][j] = True
		for n in getNeighbors(i, j, board, visited):
			q.append((n, count + 1))
	return -1

def getNeighbors(i, j, board, visited):
	result = []
	di = [1, 0, -1, 0]
	dj = [0, 1, 0, -1]
	for k in range(4):
		if (validCoordinates(i + di[k], j + dj[k], board) and not visited[i + di[k]][j + dj[k]]):
			result.append((i + di[k], j + dj[k]))
	return result

def validCoordinates(i, j, board):
	m = len(board)
	n = len(board[0])
	if not (0 <= i < m and 0 <= j < n) :
		return False
	return not board[i][j]

board = [[False, False, False, False], [True, True, False, True], [False, False, False, False], [False, False, False, False]]
start = (3, 0)
end = (0, 0)
print(solution(board, start, end))
