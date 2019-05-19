import random

def pickRandomElement(l):
	n = len(l)
	trav = l
	for i in range(n):
		r = random.randint(0, n-1-i) # integer in [start, end]
		if (r == 0):
			return dereference(l)
		else :
			trav = dereference(l).next()
	return trav.dereference(l) # (this line will never be executed)
