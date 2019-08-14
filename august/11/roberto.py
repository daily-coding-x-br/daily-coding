import math

def prime(x): # O(sqrt(n))
	for i in range(2, round(math.sqrt(x))+1):
		if (x%i == 0):
			return False
	return True

def goldbach(n): # O(n * sqrt(n))
	if (n%2 != 0):
		return None
	for i in range(2, n//2+1):
		if (prime(i) and prime(n-i)):
			return i, n-i
	return None

n = int(input())
print(goldbach(n))

def sieve(n): # O(n * log(log(n)))
	board = [True for i in range(n+1)]
	for i in range(2, round(math.sqrt(n)) + 1):
		if (not board[i]):
			continue
		for j in range(i**2, n+1, i):
			board[j] = False
	return board

def prime2(x, board):
	if (x == 1 or x == 0):
		return False
	return board[x]

def goldbach2(n): # O(n * log(log(n)))
	if (n%2 != 0):
		return None
	board = sieve(n)
	for i in range(2, n//2+1):
		if (prime2(i, board) and prime2(n-i, board)):
			return i, n-i
	return None

n = int(input())
print(goldbach2(n))
