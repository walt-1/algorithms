# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
# Return true if and only if the nodes corresponding to the values x and y are cousins.

def is_cousin(root, x, y):
  p = dict()
  d = dict()

  def dfs(node, par=None):
    if node:
      d[node.val] = 1
      p[node.val] = par
      dfs(node.left, node)
      dfs(node.right, node)
  
  dfs(root)
  return d[x] == d[y] and p[x] != p[y]