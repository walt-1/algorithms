# BST Validatoin
# Can be done using recursion (uses call stack) or an in order traversal utilizing a created stack

# Given a binary tree, determine if it is a valid binary search tree(BST).
# Assume a BST is defined as follows:
#     The left subtree of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.


from TreeNode import TreeNode

def valid(root):
    return _recurse(root)

def _recurse(node, low=float("-inf"), hi=float("inf")):
    # base case
    # null check - by default empty tree is bal/val
    if not node: return True

    val = node.val
    # asserts val is greater than low and less than hi
    if val <= low or val >= hi: return False

    # subroutine
    # checks if result of subroutine is false - false is returned
    if not _recurse(node.left, low, val): return False
    if not _recurse(node.right, val, hi): return False

    return True


valid_btree = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
invalid_btree = TreeNode(5, TreeNode(1, None, None), TreeNode(3, None, None))

print("Valid Tree: " + str(valid(valid_btree)))
print("Valid Tree: " + str(valid(invalid_btree)))
