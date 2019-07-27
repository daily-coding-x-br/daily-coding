def possibleLetters(d, s, i=0):
	if (i == len(s)):
		return [""]
	rest = possibleLetters(d, s, i+1)
	result = []
	character = int(s[i])
	mapping = d[character]
	for word in rest:
		for letter in mapping:
			result.append(letter + word)
	return result

d = {1:["a", "b", "c"], 2:["d", "e", "f"], 3:["g", "h", "i"]}
s = input()
print(possibleLetters(d, s))
