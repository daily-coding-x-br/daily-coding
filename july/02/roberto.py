# O (log(n)) time, O(1) space
def pow(x, y):
	j = y
	term = x
	result = 1
	while (j > 0):
		if (j & 1 == 1):
			result *= term
		term *= term
		j >>= 1
	return result

x = int(input())
y = int(input())
print(pow(x, y))
