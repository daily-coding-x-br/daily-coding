class Node:
  def __init__(self, data, nxt=None):
    self.data = data
    self.nxt = nxt


def length(L):
  num_nodes = 0
  it = L
  
  while it:
    it = it.nxt
    num_nodes += 1

  return num_nodes


def first_common_node(A, B):
  ans = None

  lenA = length(A)
  lenB = length(B)
  dif = abs(lenA - lenB)
  
  if lenA < lenB:
    A, B = B, A

  # Advance A by dif nodes
  count = 0
  currA = A
  while count < dif and currA and currA.nxt != None:
    currA = currA.nxt
    count += 1

  # Advance A and B simultaneously until we find the common node
  currB = B
  while currA and currB and currA.data != currB.data:
    currA = currA.data
    currB = currB.data

  if currA and currB and currA.data == currB.data:
    ans = currA

  return ans


if __name__ == "__main__":
  pass
