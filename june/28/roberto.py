def breakup(s, k):
	result = []
	i = 0
	s = s.split()
	while (i < len(s)):
		current = [s[i]]
		currentLength = len(s[i])
		while (i + 1 < len(s) and currentLength + 1 + len(s[i+1]) <= k):
			current.append(s[i+1])
			currentLength += 1 + len(s[i+1])
			i += 1
		result.append(" ".join(current))
		i += 1
	return result

def breakup2(s, k):
	result = []
	i = 0
	s = s.split()
	current = [s[i]]
	currentLength = len(s[i])
	i += 1
	while (i < len(s)):
		if (currentLength + 1 + len(s[i]) <= k):
			current.append(s[i])
			currentLength += 1 + len(s[i])
		else:
			result.append(" ".join(current))
			current = [s[i]]
			currentLength = len(s[i])
		i += 1
	result.append(" ".join(current))
	return result

s = input()
k = int(input())
print(breakup(s, k))
print(breakup2(s, k))
