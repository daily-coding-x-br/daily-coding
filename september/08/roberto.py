def sqrt(n):
	start, end = 0, n
	middle = (start + end)//2
	while (start < end):
		if (middle**2 > n):
			end = middle - 1
		elif ((middle+1)**2 <= n):
			start = middle + 1
		else:
			break
		middle = (start + end)//2
	return middle

def sqrtDecimals(n, decimals=0):
	result = sqrt(n)
	for i in range(decimals):
		start, end = 0, 9
		middle = (start + end)//2
		current = result + middle/(10**(i+1))
		while (start < end):
			if (current**2 > n):
				end = middle - 1
			elif (current**2 < n):
				start = middle + 1
			else:
				break
			middle = (start + end)//2
			current = result + middle/(10**(i+1))
		result = current
	return result

#x = list(range(25))
#y = [sqrt(n) for n in x]
#print(x)
#print(y)
n = int(input())
k = int(input())
print(sqrtDecimals(n, k))
