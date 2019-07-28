def countParenthesesToRemove(s):
	count = 0
	mininum = 0
	for i in range(len(s)):
		if (s[i] == "("):
			count += 1
		elif (s[i] == ")"):
			count -= 1
			minimum = min(mininum, count)
	result = 0
	result += -minimum # remove closing parentheses
	count += -minimum # adjust count
	result += count # remove opening parentheses
	return result

s = input()
print(countParenthesesToRemove(s))
