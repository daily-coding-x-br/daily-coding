class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(tree):
    if tree is None:
        return "#"
    return tree.val + "\\" + serialize(tree.left) + serialize(tree.right)


def deserialize(string):
    return deser_r(string, 0)


def deser_r(string, ind):
    if string[ind] == "#":
        ind += 1
        return None

    s = ""
    while string[ind] != "\\":
        s += string[ind]
        ind += 1
    ind += 1

    return Node(s, deser_r(string, ind), deser_r(string, ind))


if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))

    assert deserialize(serialize(node)).left.left.val == 'left.left'
