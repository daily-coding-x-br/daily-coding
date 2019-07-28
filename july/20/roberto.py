def canBecameNonDecreasing(l):
	if (len(l) <= 2):
		return True
	count = 0
	if (l[0] > l[1]):
		l[0] = l[1]
		count += 1
	for i in range(len(l)-2):
		if (l[i] > l[i+2]):
			return False
		if (l[i+1] > l[i+2]):
			l[i+1] = l[i]
			count += 1
		if (count > 1):
			return False
	return True

l = [int(x) for x in input().split()]
print(canBecameNonDecreasing(l))
