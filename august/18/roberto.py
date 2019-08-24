def canBeShifted(A, B):
	return B in 2 * A

def canBeShifted2(A, B):
	C = A * 2
	for i in range(len(C) - len(B) + 1):
		j = 0
		while (j < len(B) and B[j] == C[i+j]):
			j += 1
		if j == len(B):
			return True
	return False


A = input()
B = input()
print(canBeShifted2(A, B))
