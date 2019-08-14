def shortestSubstring(word, charSet):
	completeCount = 0
	charCount = {char:0 for char in charSet}
	start = 0
	end = 0
	result = float("-inf"), float("inf")
	while (start < len(word)):
		if completeCount < len(charSet):
			if (end == len(word)):
				break
			letter = word[end]
			if (letter in charSet):
				if (charCount[letter] == 0):
					completeCount += 1
				charCount[letter] += 1
			end += 1
		if completeCount == len(charSet):
			result = (start, end) if end - start < result[1] - result[0] else result
			letter = word[start]
			if (letter in charSet):
				if (charCount[letter] == 1):
					completeCount -= 1
				charCount[letter] -= 1
			start += 1
	return word[result[0]:result[1]]

word = input()
charSet = {x for x in input().split()}
print(shortestSubstring(word, charSet))
