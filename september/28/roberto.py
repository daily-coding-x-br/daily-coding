runningSum = []

def preprocess(l):
	sum = 0
	runningSum.clear()
	runningSum.append(0)
	for e in l:
		sum += e
		runningSum.append(sum)

def sum(i, j):
	return runningSum[j] - runningSum[i]

l = [int(x) for x in input().split()]
preprocess(l)
print(sum(1,3))
