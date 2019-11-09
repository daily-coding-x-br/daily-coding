def gcd(a, b):
	if (b == 0):
		return a
	return gcd(b, a%b)

def gcd_list(l):
	if (len(l) == 0):
		return None
	result = l[0]
	for i in range(2, len(l)):
		result = gcd(result, l[i])
	return result
