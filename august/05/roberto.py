def reverseList(l, start, end):
	for i in range((end - start + 1)//2):
		l[start + i], l[end - i] = l[end - i], l[start + i]

def nextPermutation(l):
	left = len(l)-1
	while (left > 0 and l[left-1] > l[left]):
		left -= 1

	successor = left
	for i in range(left, len(l)):
		if (l[i] < l[left-1]):
			continue
		successor = i if l[i] < l[successor] else successor
	l[left-1], l[successor] = l[successor], l[left-1]

	reverseList(l, left, len(l) - 1)

l = [int(x) for x in input().split()]
for i in range(24):
	nextPermutation(l)
	print(" ".join([str(x) for x in l]))
