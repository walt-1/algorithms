# Linked Lists
# Singly Linked List - consists of nodes that hold DATA, PREV, NEXT
# Doubly Linked List - consists of nodes that hold DATA, PREV, NEXT where a given node can access pred and next

# Comparison to arrays : arrays are contiguous in memory, linked lists are not.
# -----------  Array  --  Linked List
# Insertion |  O(n)   |  O(1)
# Accessing |  O(1)   |  O(n)


class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
  
class s_linked_list:
  def __init__(self):
    self.head = None

  def append(self, data):
    # creates new node
    new_node = Node(data)
    # checks if the list is empty
    if self.head == None:
      self.head = new_node
      return

    # initializes util node to the head node
    last_node = self.head
    # traverses through the list
    while last_node.next:
      # reassigns last node to its suc node until null 
      last_node = last_node.next
      
    # when the loop terminates, last_node will be set to the last item in the list 
    # and the assignment of append can be executed
    last_node.next = new_node

  def prepend(self, data):
    new_node = Node(data)
    # pointer assigned to current head in list
    new_node.next = self.head
    # change head from current head to new node
    self.head = new_node

  def insert_after(self, prev_node, data):
    # creates node
    # checks if node to insert after is in list
    if prev_node == None:
      print("Node is not in list")
    else:
      # initializes new node with data to insert
      new_node = Node(data)
      # set new nodes pointer to prev nodes following node
      new_node.next = prev_node.next
      # set prev_node next pointer to new node
      prev_node.next = new_node

  # has to turn the next pointers around because there is only a single direction
  def reverse(self):
    prev_node = None
    cur_node = self.head
    next_node = None

    while cur_node:
      next_node = cur_node.next # save next
      cur_node.next = prev_node  # reverse
      # At each step, we create a prev pointer because we
      # do not have constant time access to prev node in 
      # the structure of a singly linked list
      prev_node = cur_node  # save next
      cur_node = next_node
    
    return prev_node
    

  def print_list(self):
    cur_node = self.head
    
    while cur_node:
      # prints data of current node
      next_data = cur_node.next.data if cur_node.next != None else "None"
      print(cur_node.data + " -> " + next_data)
      # moves cur_node value to next node in the list
      cur_node = cur_node.next


sl_list = s_linked_list()
sl_list.append('A')
sl_list.append('B')
sl_list.append('C')
sl_list.prepend('D')
sl_list.insert_after(sl_list.head.next, 'E')
sl_list.print_list()
sl_list.reverse()
