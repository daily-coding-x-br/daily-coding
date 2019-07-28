import math

def count(n, x):
	result = 0
	for i in range(max(1, x//n), min(n, round(math.sqrt(x))) + 1):
		if ((x//i)*i == x and x//i <= n):
			result += 1
	result *= 2
	sqr = (round(math.sqrt(x)))
	if (sqr**2 == x and sqr <= n):
		result -= 1
	return result

n, x = [int(x) for x in input().split()]
print(count(n, x))
