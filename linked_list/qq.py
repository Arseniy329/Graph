class Node:
  def init(self, data):
    self.data = data
    self.next = None

def append(head):
  cur_node = head
  while cur_node:
    print(cur_node.data, end=" -> ")
    currentNode = currentNode.next

def insertNodeAtPosition(head, newNode, position):
  if position == 1:
    newNode.next = head
    return newNode

  currentNode = head
  for _ in range(position - 2):
    if currentNode is None:
      break
    currentNode = currentNode.next

  newNode.next = currentNode.next
  currentNode.next = newNode
  return head

node1 = Node(7)
node2 = Node(3)
node3 = Node(2)
node4 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4

print("Original list:")
append(node1)

newNode = Node(97)
node1 = insertNodeAtPosition(node1, newNode, 2)

print("\nAfter insertion:")
append(node1)
