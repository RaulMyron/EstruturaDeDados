

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

no1 = Node(5)
no2 = Node(9)

no1.next = no2
print(no1.next)