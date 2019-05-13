def query(s, d):
	root = d
	trav = root
	prefix = []
	for i in range(len(s)):
		if (trav.hasChild(s[i])):
			trav = trav.getChild(s[i])
			prefix.append(s[i])
		else:
			return []
	return getAllWords3(trav, prefix)

def getAllWords(node, prefix):
	result = []
	if (node.end):
		result.append("".join(prefix))
	characters = node.getCharacters()
	for c in characters:
		prefix.append(c)
		child = node.getChild(c)
		l = getAllWords(child, prefix)
		prefix.pop()
		for word in l:
			result.append(word)
	return result

def getAllWords2(node, prefix, result=[]):
	if (node.end):
		result.append("".join(prefix))
	characters = node.getCharacters()
	for c in characters:
		prefix.append(c)
		child = node.getChild(c)
		getAllWords2(child, prefix, result)
		prefix.pop()
	return result

def getAllWords3(node, prefix):
	def helper(node, prefix, result):
		if (node.end):
			result.append("".join(prefix))
		characters = node.getCharacters()
		for c in characters:
			prefix.append(c)
			child = node.getChild(c)
			helper(child, prefix, result)
			prefix.pop()
	result = []
	helper(node, prefix, result)
	return result


def getTRI(l):
	root = Node()
	for s in l:
		trav = root
		for i in range(len(s)):
			if (not trav.hasChild(s[i])):
				trav.addChild(s[i])
			trav = trav.getChild(s[i])
		trav.end = True
	return root

class Node:
	def __init__(self):
		self.d = {}
		self.end = False
		self.parent = None

	def addChild(self, c):
		self.d[c] = Node()
		self.d[c].parent = self

	def hasChild(self, c):
		return c in self.d

	def getChild(self, c):
		return self.d[c]

	def getCharacters(self):
		return self.d


l = input().split()
q = input()
d = getTRI(l)
print(query(q, d))
