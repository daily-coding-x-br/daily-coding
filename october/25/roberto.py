def mapping(s1, s2):
	d = {}
	if (len(s1) != len(s2)):
		return False
	for i in range(len(s1)):
		c1 = s1[i]
		c2 = s2[i]
		if c1 in d and d[c1] != c2:
			return False
		d[c1] = c2
	return True

s1 = input()
s2 = input()
print(mapping(s1, s2))
