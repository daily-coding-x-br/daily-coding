class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    s = ""
    if (root is not None):
        s += root.val
        s += serialize(root.left)
        s += serialize(root.right)
    return "(" + s + ")"

def deserialize_rec(s, i):
    i = i+1  # Skipping (

    # Parsing val
    val = ""
    while (s[i] != '(' and s[i] != ')'):
        val += s[i]
        i = i+1
    if (len(val) == 0):
        i = i+1
        return None

    # Creating node recursively
    node = Node(val)
    node.left = deserialize_rec(s, i)
    node.right = deserialize_rec(s, i)

    i = i+1  # Skipping )
    return node

def deserialize(s):
    return deserialize_rec(s, 0) 

if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'

