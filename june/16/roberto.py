def rand7():
	r = rand5()*5 + rand5() # r uniformly distributed in [0, 24]
	return r%7 if r < 21 else rand7()

# implement randN given randM
def randN():
	r = randM()*M + randM()
	return r%N if r < ((M**2)//N)*N else randN()
