def rand7():
	r = rand5()*5 + rand5() # r uniformly distributed in [0, 24]
	return r%7 if r < 21 else rand7()

# implement randN given randM
def randN():
	r, maxR = 0, 0
	while (maxR < N):
		r *= M;
		r += randM()
		maxR *= M;
	# r is uniformly distributed in [0, maxR - 1], with maxR >= N
	return r%N if r < ((maxR)//N)*N else randN()
