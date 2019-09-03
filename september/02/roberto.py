def count(char, s):
	return len([c for c in s if c == char])

def representsNumber(s):
	allowed = [str(x) for x in range(10)] + ["e", ".", "-"]
	for c in s:
		if c not in allowed:
			return False
	minusCount = count("-", s)
	if (minusCount > 1):
		return False
	if (minusCount == 1):
		if (len(s) == 1 or s[0] != "-"):
			return False
	dotCount = count(".", s)
	if (dotCount > 1):
		return False
	eCount = count("e", s)
	if (eCount > 1):
		return False
	if (eCount == 1):
		if (s[0] == "e" or s[-1] == "e"):
			return False
	if (dotCount == 1 and eCount == 1):
		for c in s:
			if (c == "e"):
				return False
			elif (c == "."):
				break
	return True

s = input()
print(representsNumber(s))
