def combinations(n, k):
	if (k > n//2):
		k = n - k
	result = 1
	for i in range(k):
		result *= (n-i)/(k-i)
	return result

def rounds(n, d={}):
	if (n <= 1):
		return 0
	if (n in d):
		return d[n]
	sum = 0
	for i in range(n):
		sum += combinations(n, i)*rounds(i, d)
	sum = (sum*(2**(-n)) + 1)/(1 - 2**(-n))
	d[n] = sum
	return d[n]

n = int(input())
print(rounds(n))

# f(n) = 1 + sum([f(k) * combinations(n, k) for k in range(n+1)]) / 2**n
