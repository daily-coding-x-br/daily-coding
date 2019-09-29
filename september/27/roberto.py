def grayCode(n):
	if (n == 0):
		return [""]
	smaller = grayCode(n-1)
	result = []
	for e in smaller:
		result.append("0" + e)
	for e in reversed(smaller):
		result.append("1" + e)
	return result

n = int(input())
print(grayCode(n))
