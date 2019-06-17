def subsetSum(S, k):
	S.sort(reverse=True)
	memory = {}
	def recurse(k, i=0):
		if (k, i) in memory:
			return memory[k, i]
		if (k == 0):
			return [], True
		if (i == len(S)):
			return [], False
		for j in range(i, len(S)):
			if (S[j] <= k):
				result = recurse(k-S[j], j+1)
				if (result[1] == True):
					memory[k, i] = ([S[j]] + result[0]), True
					return memory[k, i]
		memory[k, i] = [], False
		return memory[k, i]
	result = recurse(k)
	return result[0] if result[1] else "null"

S = [int(x) for x in input().split()]
k = int(input())
print(subsetSum(S, k))
