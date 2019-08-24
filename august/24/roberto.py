def reverseWord(l, start, end):
	for i in range((end - start)//2):
		l[start + i], l[end - 1 - i] = l[end - 1 - i], l[start + i]

def reverseDelimiters(l, delimiters):
	start, end = 0, len(l) - 1
	while (start < end):
		while (start < end and l[start] not in delimiters):
			start += 1
		while (start < end and l[end] not in delimiters):
			end -= 1
		l[start], l[end] = l[end], l[start]
		start, end = start + 1, end - 1

def reverseWords(s, delimiters):
	l = [c for c in s]
	reverseWord(l, 0, len(l))
	reverseDelimiters(l, delimiters)
	start, end = 0, 0
	while (start < len(l)):
		while (end < len(l) and l[end] not in delimiters):
			end += 1
		reverseWord(l, start, end)
		start, end = end + 1, end + 1
	return "".join(l)

s = input()
delimiters = {x for x in input().split()}
print(reverseWords(s, delimiters))
