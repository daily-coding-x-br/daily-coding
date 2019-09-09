def printSteps(n, left=1, middle=2, right=3):
	if (n <= 0):
		return
	printSteps(n-1, left, right, middle)
	print("Move " + str(left) + " to " + str(right))
	printSteps(n-1, middle, left, right)

n = int(input())
printSteps(n)
