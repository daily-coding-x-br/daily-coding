def balanced(s):
	openCount = 0
	asteriskCount = 0
	for c in s:
		if (c == "*"):
			asteriskCount += 1
		elif (c == "("):
			openCount += 1
		elif (c == ")"):
			openCount -= 1
		while openCount < 0 and asteriskCount > 0:
			openCount += 1
			asteriskCount -= 1
		if openCount < 0:
			return False
	return asteriskCount >= openCount

s = input()
print(balanced(s))
