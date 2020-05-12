# class node
class node:
  def __init__(self, value = None):
    self.value = value
    self.right_child = None
    self.left_child = None
# end node

# class bst
class binary_search_tree:
  def __init__(self):
    self.root = None
  
  # height - params: self
  def height(self):
    if self.root != None:
      # call private method
      return self._height(self.root, 0)
    else:
      return 0
  
  # private height - params: self, cur_node, cur_height
  def _height(self, cur_node, cur_height):
    # checks if current node doesnot exist in which case the current height is returned
    if cur_node == None: return cur_height

    # define left and right height, recursing down each side by passing an incremented height to itself
    left_height = self._height(cur_node.left_child, cur_height + 1)
    right_height = self._height(cur_node.right_child, cur_height + 1)

    # returns a max comparison of each side
    return max(left_height, right_height)

  # insert - params: self, value
  def insert(self, value):
    # check if the tree has a root
    if self.root == None:
      ## assign root using node class
      self.root = node(value)
    else: 
      # call private insertion method
      self._insert(value, self.root)

  # private insert - params: self, value, cur_node
  def _insert(self, value, cur_node):
    # if value < cur_node.value
    if value < cur_node.value:
      # if the cur_node.left_child does not exists
      if cur_node.left_child == None:
        # place value using node class
        cur_node.left_child = node(value)
      else:
        # recurse down the left side of the tree to place value
        self._insert(value, cur_node.left_child)
    # if value > cur_node.value
    elif value > cur_node.value:
      # if the cur_node.right_child does not exists
      if cur_node.right_child == None:
        # place value using node class
        cur_node.right_child = node(value)
      else:
        # recurse down the left side of the tree to place value
        self._insert(value, cur_node.right_child)
    else:
      # else print out node already exists
      print("Value exists in tree")
   
  # print - params: self
  def print_tree(self):
    # check if tree does not have a root
    if self.root != None:
      # call private print method
      self._print_tree(self.root)

  # private print - params: self, cur_node
  def _print_tree(self, cur_node):
    # check if cur_node.value is null
    if cur_node != None:
      # perform in order traversal
      self._print_tree(cur_node.left_child)
      # print node value
      print(str(cur_node.value))
      self._print_tree(cur_node.right_child)

  # search
  def search(self, value):
    # check if the root doesnt equal none
    if self.root != None:
      return self._search(value, self.root)
    # else return False to user
    else:
      return False

  def _search(self, value, cur_node):
    # checks value exists and matches
    if value == cur_node.value:
      return True
    # checks if value is less than curnode value and MAKES SURE left child exists
    elif value < cur_node.value and cur_node.left_child != None:
      return self._search(value, cur_node.left_child)
    # checks if value is less than curnode value and MAKES SURE left child exists
    elif value > cur_node.value and cur_node.right_child != None:
      return self._search(value, cur_node.right_child)
    # if not found - worst case returns false
    return False

  # seeds tree with random ints
  def seed(self, n_elems = 10, max_n = 20):
    # import randnum
    from random import randint
    for _ in range(n_elems):
      # define current element with max n
      cur_elem = randint(0, max_n)
      # insert into the tree
      self.insert(cur_elem)
# end bst

# calls
tree = binary_search_tree()
tree.seed()
tree.print_tree()
print("is a four " + str(tree.search(4)))
print("Tree Height: " + str(tree.height()))