def naive(m, s):
	i = 0
	while (i < len(m)):
		j = 0
		while (j < len(m[i]) - len(s) + 1):
			k = 0
			while (k < len(s) and m[i][j + k] == s[k]):
				k += 1
			if (k == len(s)):
				return True
			j += 1
		i += 1

	j = 0
	while (j < len(m[0])):
		i = 0
		while (i < len(m) - len(s) + 1):
			k = 0
			while (k < len(s) and m[i + k][j] == s[k]):
				k += 1
			if (k == len(s)):
				return True
			i += 1
		j += 1

	return False

def hash(s):
	result = 0
	for i in range(len(s)):
		result *= 27
		result += ord(s[i]) - ord("a") + 1
	return result

def better(m, s):
	hs = hash(s)
	i = 0
	while (i < len(m)):
		j = 0
		h = hash(m[i][j:j+len(s)])
		while (h != hs and j < len(m[i]) - len(s)):
			h -= (ord(m[i][j]) - ord("a") + 1) * 27**(len(s)-1)
			h *= 27
			h += ord(m[i][j+len(s)]) - ord("a") + 1
			j += 1
		if (h == hs):
			return True
		i += 1

	j = 0
	while (j < len(m[0])):
		i = 0
		h = hash( [m[i+k][j] for k in range(len(s))] )
		while (h != hs and i < len(m) - len(s)):
			h -= (ord(m[i][j]) - ord("a") + 1) * 27**(len(s)-1)
			h *= 27
			h += ord(m[i+len(s)][j]) - ord("a") + 1
			i += 1
		if (h == hs):
			return True
		j += 1

	return False

m = [['F', 'A', 'C', 'I'], ['O', 'B', 'Q', 'P'], ['A', 'N', 'O', 'B'], ['M', 'A', 'S', 'S']]
print(naive(m, "FOAM"))
print(naive(m, "MASS"))
print(better(m, "FOAM"))
print(better(m, "MASS"))
