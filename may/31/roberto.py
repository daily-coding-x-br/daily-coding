def encode(s):
	result = []
	count = 0
	i = 0
	last = s[0]
	while (i < len(s)):
		if (s[i] == last):
			count += 1
		else:
			result.append(str(count) + last)
			count = 1
			last = s[i]
		i += 1
	result.append(str(count) + last)
	return "".join(result)

def decode(s):
	result = []
	count = 0
	i = 0
	while (i < len(s)):
		if (s[i].isdigit()):
			count *= 10
			count += int(s[i])
		else:
			result.append(s[i] * count)
			count = 0
		i += 1
	return "".join(result)


s = input()
print(encode(s))
print(decode(encode(s)))
