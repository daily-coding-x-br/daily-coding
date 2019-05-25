class Node:
	def __init__(self):
		self.d = {}
		self.endOfWord = False

	def addChild(self, c):
		self.d[c] = Node()

	def hasChild(self, c):
		return c in self.d

	def getChild(self, c):
		return self.d[c]

def getTrie(l):
	root = Node()
	for s in l:
		trav = root
		for i in range(len(s)):
			if (not trav.hasChild(s[i])):
				trav.addChild(s[i])
			trav = trav.getChild(s[i])
		trav.endOfWord = True
	return root

def solution(l, s):
	trie = getTrie(l)
	return helper(trie, s)

def helper(trie, s, start=0, mem={}): # O(n) time, O(n) space
	if (start in mem):
		return mem[start]
	trav = trie
	i = start
	while (i < len(s)):
		if (trav.hasChild(s[i])):
			trav = trav.getChild(s[i])
			i += 1
		else:
			return None

		if (trav.endOfWord):
			if (i == len(s)):
				mem[start] = [s[start:i]]
				return [s[start:i]]
			rest = helper(trie, s, i, mem)
			if (rest is not None):
				rest.append(s[start:i])
				mem[start] = rest
				return rest

l = input().split()
s = input()
print(solution(l, s))
