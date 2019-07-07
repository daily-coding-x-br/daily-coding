def printSpiral(m):
	def helper(m, i_s=0, i_e=len(m)-1, j_s=0, j_e=len(m[0])-1):
		if (i_s > i_e or j_s > j_e):
			return

		if (i_s == i_e):
			for j in range(j_s, j_e+1):
				print(m[i_s][j])
			return

		if (j_s == j_e):
			for i in range(i_s, i_e+1):
				print(m[i][j_s])
			return

		for j in range(j_s, j_e):
			print(m[i_s][j])

		for i in range(i_s, i_e):
			print(m[i][j_e])

		for j in reversed(range(j_s+1, j_e+1)):
			print(m[i_e][j])

		for i in reversed(range(i_s+1, i_e+1)):
			print(m[i][j_s])

		helper(m, i_s+1, i_e-1, j_s+1, j_e-1)

	helper(m)

m = [[1,  2,  3,  4,  5], [6,  7,  8,  9,  10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
print(m[0])
print(m[1])
print(m[2])
print(m[3])
printSpiral(m)
