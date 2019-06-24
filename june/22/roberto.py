def shuffle(l):
	n = len(l)
	for i in range(52):
		r = rand(n - i) + i - 1 # uniformly distributed in [i, n-1]
		l[i], l[r] = l[r], l[i]
	return l
