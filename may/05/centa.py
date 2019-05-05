# O(n) runtime and O(n) space complexity
# uniquely identify each node with and integer and add
# the ones that appear to the code
# used recursion but an iterative solution is possible
# by: Centa

from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def _serialize(root, id, code_builder):
    if root:
        code_builder.append("{:}:{:}".format(id, root.val))
        _serialize(root.left, 2*id, code_builder)
        _serialize(root.right, 2*id+1, code_builder)


def serialize(root):
    code_builder = []

    _serialize(root, 1, code_builder)

    return " ".join(code_builder)


def _deserialize(id, node_map):
    if id in node_map.keys():
        node = Node(node_map[id])
        node.left = _deserialize(2*id, node_map)
        node.right = _deserialize(2*id+1, node_map)
        return node
    return None


def deserialize(code):
    node_map = { int(s.split(":")[0]):s.split(":")[1] for s in code.split(" ") }

    return _deserialize(1, node_map)


if __name__ == "__main__":
    # driver code
    node = Node('root', Node('left', Node('left.left')), Node('right'))

    assert deserialize(serialize(node)).left.left.val == 'left.left'
