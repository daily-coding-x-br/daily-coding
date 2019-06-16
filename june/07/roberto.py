def getSecondLargest(root):
	trav = root
	while (trav.right):
		trav = trav.right

	if (not trav.left):
		return trav.parent.value

	trav = trav.left
	while (trav.right):
		trav = trav.right

	return trav.value
