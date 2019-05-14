class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countUnivalTrees(node): # returns unival tree count
	return helper(node)[0]

def helper(node): # returns (unival tree count, wether current node is a unival tree)
	if node is None:
		return 0, True

	left = helper(node.left)
	right = helper(node.right)

	univTreeCount = left[0] + right[0]

	isUnivTree = True
	if (node.left and not (node.left.val == node.val and left[1])):
		isUnivTree = False
	if (node.right and not (node.right.val == node.val and right[1])):
		isUnivTree = False

	if isUnivTree: univTreeCount += 1
	return univTreeCount, isUnivTree

root = Node(0, Node(1, None, None), Node(0, Node(1, Node(1, None, None), Node(1, None, None)), Node(0, None, None)))
print(countUnivalTrees(root))
