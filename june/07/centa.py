class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right



def get_largest(root):
    largest = root
    
    while largest.right != None:
        largest = largest.right
    
    return largest

def get_second_largest(root):
    # assert size of tree > 1

    # get the largest node
    largest = get_largest(root)

    # descend and diverge just before the second largest
    second = root
    if largest != root:
        while second.right != largest:
            second = second.right
    
    if not second.left:
        return second
    else:
        return get_largest(second.left)
