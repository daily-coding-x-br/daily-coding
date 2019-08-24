def reverseWord(l, start, end):
	for i in range((end - start)//2):
		l[start + i], l[end - 1 - i] = l[end - 1 - i], l[start + i]

def reverseWords(s):
	l = [c for c in s]
	reverseWord(l, 0, len(l))
	start, end = 0, 0
	while (start < len(l)):
		while (end < len(l) and l[end] != " "):
			end += 1
		reverseWord(l, start, end)
		start, end = end + 1, end + 1
	return "".join(l)

s = input()
print(reverseWords(s))
