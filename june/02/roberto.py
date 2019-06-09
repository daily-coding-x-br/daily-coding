def distance(s1, s2):
	m = [[0 for j in range(len(s1))] for i in range(len(s2))]
	m[0][0] = 1 if s1[0] != s2[0] else 0
	for i in range(1, len(s2)):
		m[i][0] = m[i-1][0] + 1
	for j in range(1, len(s1)):
		m[0][j] = m[0][j-1] + 1
	for i in range(1, len(s2)):
		for j in range(1, len(s1)):
			a = m[i-1][j] + 1
			d = m[i][j-1] + 1
			r = m[i-1][j-1] + (1 if s1[j] != s2[i] else 0)
			m[i][j] = min(a, d, r)
	return m[len(s2)-1][len(s1)-1]

s1 = input()
s2 = input()
print(distance(s1, s2))
