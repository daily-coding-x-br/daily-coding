def balanced(s):
	stack = []
	opening = { ")" : "(" , "}" : "{" , "]" : "[" }
	for c in s:
		if (c == "(" or c == "{" or c == "["):
			stack.append(c)
		elif (c == ")" or c == "}" or c == "]"):
			if (len(stack) == 0 or stack.pop() != opening[c]):
				return False
	return (len(stack) == 0)

s = input()
print(balanced(s))
