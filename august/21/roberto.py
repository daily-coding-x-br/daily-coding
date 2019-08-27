def findStartingIndices(w, s):
	targetCount = {}
	def fill(targetCount, w):
		for letter in w:
			targetCount[letter] = 1 if letter not in targetCount else (1 + targetCount[letter])
	fill(targetCount, w)

	def add(count, matchingCount, letter):
		if letter not in targetCount:
			return
		count[letter] = 1 if letter not in count else (1 + count[letter])
		if (count[letter] == targetCount[letter]):
			matchingCount[0] += 1
	def remove(count, matchingCount, letter):
		if letter not in targetCount:
			return
		if (count[letter] == targetCount[letter]):
			matchingCount[0] -= 1
		count[letter] -= 1

	matchingCount = [0]
	result = []
	count = {}
	start, end = 0, 0
	while (end < len(w)):
		add(count, matchingCount, s[end])
		end += 1
	while (end < len(s)):
		if matchingCount[0] == len(targetCount):
			result.append(start)
		remove(count, matchingCount, s[start])
		add(count, matchingCount, s[end])
		start += 1
		end += 1
	if matchingCount[0] == len(targetCount):
		result.append(start)
	return result

w = input()
s = input()
print(findStartingIndices(w, s))
